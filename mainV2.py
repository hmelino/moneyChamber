import datetime
import pickle
import requests
import sys
import os
import time

def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')
		
today=datetime.datetime.today().date()

class CreatePortfolio:
	totalPortfolio={}
	oldestDay=None
	db={}
	orders=None
	
	def __init__(self):
		self.loadStatement('statementV2.txt')
		self.orders=self.loadOrders()
		self.dividend=self.loadDividends()
		self.oldestDay=min([self.db[stock].date for stock in self.db])
		for stock in self.db:
			self.addPrices(stock)
		self.updateTotalPortfolio()
		self.graph()
		
	def loadDividends(self):
		
		try:
			print("Loading dividends")
			from MoneyChamber.dividendPaid import data
			return data
		except ModuleNotFoundError:
			print("Missing dividendPaid.py file")
			return {}
			
	def graph(self):
		def convertDate(s):
			return 
			
		def xlabels():
			multiplier=0.166
			dates=list(self.totalPortfolio.keys())
			tlen=len(dates)
			datesLabels=[dates[int(tlen*(k*0.1999))] for k in range(6)]
			fig,ax=plt.subplots()
			plt.plot([v for v in self.totalPortfolio.values()])
			ax.set_xticklabels(datesLabels)
		
		from matplotlib import pyplot as plt
		xlabels()
		plt.axhline(0)
		plt.xlabel("Date")
		plt.show()
		xlabels()
		
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
			print("Loading orders")
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
			date=(self.oldestDay+datetime.timedelta(day)).date()
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
		try:
			data=open('MoneyChamber/statementV2.txt','r').readlines()
		except FileNotFoundError:
			data=open('statementV2.txt','r').readlines()
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
					from MoneyChamber.sensData import apiKey
					return apiKey
				except ModuleNotFoundError:
					from sensData import apiKey
					return apiKey
				else:
					print('Please create sensData.py file inside MoneyChamber folder')
					sys.exit()
				"""
				except ImportError:
					print("Please create variable 'apiKey=your_worldtradingdata.com_api_key' inside sensData.py")
					sys.exit()
			"""
			apiKey=importApiKey()
			todayUnixTime=time.time()
			def downloadFreshStockData():
				return requests.get(f'https://api.worldtradingdata.com/api/v1/history?symbol={stockName}.L&sort=newest&api_token={apiKey}').json()['history']
			
			if stockName == "BT":
				stockName+=".A"
			path=f"pickle/{stockName}.pickle"
			res=pickle.load(open(path,"rb"))

			try:
				path=f"pickle/{stockName}.pickle"
				res=pickle.load(open(path,"rb"))
				if todayUnixTime - os.path.getmtime(path) > 86400:
					res=downloadFreshStockData()
			except (KeyError):
				res = downloadFreshStockData()
				print("Downloaded "+str(stockName))
				pickle.dump(res,open(f"pickle/{stockName}.pickle",'wb'))
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

			if day in ordersData[stockName]:
				basePrice,amount=newBasePrice()
				
			if day in priceData:
				stockPrice=float(priceData[day]['close'])
			self.db[stockName].history[day]=Day(basePrice,amount,stockPrice,etf,dividendTotal)
				

pass
