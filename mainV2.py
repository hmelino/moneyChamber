import datetime
import pickle
import requests
import sys
import os
import time

def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')
		
today=datetime.datetime.today().date()

class Portfolio:
	totalPortfolio={}
	oldestDay=None
	db={}
	orders=None
	profit=0
	
	def __init__(self):
		self.loadStatement('statement.txt')
		self.orders=self.loadOrders()
		self.dividend=self.loadDividends()
		self.oldestDay=min([self.db[stock].date for stock in self.db])
		for stock in self.db:
			self.addPrices(stock)
		self.updateTotalPortfolio()
		self.graph()
		self.profit=list(self.totalPortfolio.values())[-1]
		
	def loadDividends(self):
		try:
			#print("Loading dividends")
			from moneyChamber.dividendPaid import data
			return data
		except ModuleNotFoundError:
			print("Missing dividendPaid.py file")
			return {}
			
	def graph(self):
		from moneyChamber.profitLossGraph import optimizeData
		import numpy as np
		from matplotlib import pyplot as plt
		spacing=5
		dayValues=[v for v in self.totalPortfolio.values()]
		dates=list(self.totalPortfolio.keys())
		datesArray=dates
		_,ax=plt.subplots()
		
		profit,loss=optimizeData(dayValues)
		dMultiplier=int(len(dates)/(spacing))
		datesTicks=[dates[v*dMultiplier] for v in range(spacing)]
		datesTicks.insert(0,0)
		datesTicks.append(dates[-1])
		plt.plot(profit,linewidth=2,color='#7AA8AC',label='Profit')
		plt.plot(loss,linewidth=2,color='#C56C74',label='Loss')
		#print(plt.rcParams.keys())
		bgColor='#154F55'
		plt.rcParams['axes.facecolor']=bgColor
		plt.rcParams['axes.edgecolor']=bgColor
		plt.rcParams['figure.facecolor']=bgColor
		plt.rcParams['figure.edgecolor']=bgColor
		plt.rcParams['savefig.facecolor']=bgColor
		plt.rcParams['savefig.edgecolor']=bgColor
		plt.rcParams['text.color']='white'
		plt.rcParams['xtick.color']='white'
		plt.rcParams['ytick.color']='white'
		plt.rcParams['patch.edgecolor']='red'
		plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
		plt.rcParams['legend.loc']='upper left'
		
		
		multiplierV2=len(profit)/len(list(self.totalPortfolio.keys()))
		
		def showMonths():
			#list with first day of month index N
			fDayPositions=[]
			pDates=list(self.totalPortfolio.keys())
			for day in range(len(pDates)):
				if pDates[day][8:10]=='01':
					fDayPositions.append(day)
			fDayPositionsX=[v*multiplierV2 for v in fDayPositions]
			for n in fDayPositionsX:
				plt.axvline(n,color='white',alpha=0.1)
		def showYears():
			nYPositions={}
			pDates=list(self.totalPortfolio.keys())
			savedYear=pDates[0][0:4]
			#nYPositions.append(savedYear)
			for d in range(len(pDates)):
				if pDates[d][0:4]!=savedYear:
					savedYear=pDates[d][0:4]
					nYPositions[savedYear]=d
			for year in nYPositions.values():
				plt.axvline(year*multiplierV2,color='white',alpha=0.5)
			
				
			
			
		showYears()
		showMonths()
		
		
		ax.xaxis.set_major_locator(plt.MultipleLocator(len(profit)/spacing))
		ax.set_xticklabels(datesTicks)
		plt.legend()
		plt.show()
		
	def loadDeposits(self):
		try:
			from moneyChamber.deposits import cashDeposits
			return cashDeposits
		except ModuleNotFoundError:
			return []
			
	def loadOrders(self):
		def createOrders():
			""" Create orders data if orders.py is not provided """
			d=self.db
			data={d[s].name:{strDay(d[s].date):[d[s].amount,d[s].price]} for s in d}

			#adjust prices for non ETF
			for stock in data.keys():
				etfs=self.Stock.__etfs__
				if stock not in etfs:
					for date in data[stock].keys():
						secondPart=data[stock][date]
						secondPart[1]*=100
			return data

		try:
			#print("Loading orders")
			from MoneyChamber.orders import data
			return data
			
		except ModuleNotFoundError:
			return createOrders()
			
		except ImportError:
			print('Create variable "data" inside of orders.py with all stock orders')
			
	def updateTotalPortfolio(self):
		deposits=self.loadDeposits()
		totalDeposits=0
		for day in range((today-self.oldestDay.date()).days):
			stringDay=strDay(self.oldestDay+datetime.timedelta(day))
			totalForDay=0
			if stringDay in deposits:
					totalDeposits+=deposits[stringDay]
			for stockName in self.db:
				if stringDay in self.db[stockName].history:
					totalForDay+=self.db[stockName].history[stringDay].profit
			self.totalPortfolio[stringDay]=totalForDay

	class Stock:
		__etfs__=['VUKE','VMID']
		def __init__ (self,l):
			self.date=self.processDate(l)
			self.buySell=l[3]
			self.amount=float(l[4])
			self.name=l[5]
			self.price=float(l[6])
			buyRange=(today-self.date.date()).days
			self.history={strDay((self.date+datetime.timedelta(d)).date()):0 for d in range(buyRange)}
			self.updateETF()
			self.dividendTotal=0

		def processDate(self,l):
			return datetime.datetime.strptime(l[2],'%Y.%m.%d %H:%M')

		def updateETF(self):
			if self.name in self.__etfs__:
				self.etf=True
			else:
				self.etf=False
				self.price/=100

	def loadStatement(self,url):

		data=open('moneyChamber/statement.txt','r')
		result = [l.split('\t') for l in data]
		for d in result:
			self.db[d[5]]=self.Stock(d)

	def addPrices(self,stockName):
		class Day:
			def __init__(self,basePrice,amount,stockPrice,etf,dividend):
				if etf == False:
					stockPrice/=100
					basePrice/=100
				self.profit=round(((stockPrice-basePrice)*amount)+dividend,3)
				self.amount=amount
				self.stockPrice=stockPrice
				self.basePrice=basePrice
				self.dividendPaid=dividend
		
		def oneTimeConnection(stockName=stockName):
			def importApiKey():
				try:
					from moneyChamber.sensData import apiKey
					return apiKey
				except ModuleNotFoundError:
					print('Please create sensData.py file inside MoneyChamber folder and create variable apiKey="your_worldtradingdata.com_api_key" inside sensData.py')
					sys.exit()

			apiKey=importApiKey()
			todayUnixTime=time.time()
			def downloadFreshStockData():
				try:
					data=requests.get(f'https://api.worldtradingdata.com/api/v1/history?symbol={stockName}.L&sort=newest&api_token={apiKey}').json()['history']
					return data
				except ConnectionError:
					print('Connection error')
			
			if stockName == "BT":
				stockName+=".A"
			path=f"moneyChamber/pickle/{stockName}.pickle"
			try:
				res=pickle.load(open(path,"rb"))
				if todayUnixTime - os.path.getmtime(path) > 86400:
					res=downloadFreshStockData()
					#print(f"Old data for {stockName}, dowloaded new one")
					pickle.dump(res,open(path,'wb'))
			except (FileNotFoundError):
				#print(f"didnt find saved {stockName}")
				res = downloadFreshStockData()
				#print("Downloaded "+str(stockName))
				pickle.dump(res,open(f"moneyChamber/pickle/{stockName}.pickle",'wb'))
			return res
			
		def newBasePrice():
			if day != firstDay:
				bfAmount=amount
				newAmount,newPrice=ordersData[stockName][day]
				bfPrice=basePrice
				totalBefore=bfAmount*bfPrice
				totalNew=newAmount*newPrice
				totalAmount=bfAmount+newAmount
				newBasePrice=(totalBefore+totalNew)/totalAmount
				return round(newBasePrice,3),totalAmount
			return basePrice,amount
		
		priceData=oneTimeConnection()
		ordersData=self.orders
		dividendsData=self.dividend
		stockPrice=0
		dividendTotal=0
		firstDay=strDay(self.db[stockName].date)
		amount=float(ordersData[stockName][firstDay][0])
		basePrice=float(ordersData[stockName][firstDay][1])
		etf=self.db[stockName].etf
		for day in self.db[stockName].history.keys():
			if dividendsData:
				if day in dividendsData[stockName]:
					dividendTotal+=dividendsData[stockName][day]
					self.db[stockName].dividendTotal+=dividendsData[stockName][day]

			if day in ordersData[stockName]:
				basePrice,amount=newBasePrice()
				
			if day in priceData:
				stockPrice=float(priceData[day]['close'])
			self.db[stockName].history[day]=Day(basePrice,amount,stockPrice,etf,dividendTotal)
				

pass
