import datetime
import pickle
import requests
import sys
import os
import time
import json

def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')
		
today=datetime.datetime.today().date()

class Portfolio:
	import matplotlib.pyplot
	plt=matplotlib.pyplot
	totalPortfolio={}
	oldestDay=None
	db={}
	profit=0
	totalDividendsDict={}
		
	def countYeld(self):
		class MonthlyYeld:
			def __init__(self,divIncome,total):
				self.divIncome=round(divIncome,2)
				self.total=round(total,2)
				self.yeld=round((divIncome/total)*100,3)
				
		def nextMonth(date):
			date-=datetime.timedelta(32)
			try:
				return (datetime.datetime(date.year,date.month,today.day).date())
			except ValueError:
				return (datetime.datetime(date.year,date.month,today.day-3).date())
		def getNewestDay():
			d=list(self.totalPortfolio.keys())[-1]
			return (datetime.datetime.strptime(d,'%Y-%m-%d')).date()
		
		newestDay=getNewestDay()
		day=newestDay
		divPay=[]
		deposits=[]
		yeld=[]
		while day > self.oldestDay:
			totalIncome=0
			totalWorth=0
			for s in self.db:
				path=self.db[s].history
				if day in path:
					amount=path[day].amount
					bPrice=path[day].basePrice
					total=amount*bPrice
					totalIncome+=(total*self.db[s].yeld)
					totalWorth+=total
			o=MonthlyYeld(totalIncome,totalWorth)
			print(day,o.divIncome,o.total,o.yeld)
			day=nextMonth(day)
		
			
	def countYearlyDivYelds(self):
		def oldestNewestDay():
			newestDay=list(path.keys())[-1]
			yearAgo=newestDay-datetime.timedelta(365)
			if yearAgo not in path:
				yearAgo=self.db[s].date
			return yearAgo,newestDay
			
		for s in self.db:
			path=self.db[s].history
			yearAgo,newestDay=oldestNewestDay()
			processedDay=yearAgo
			dividend=0
			totalYeld=0
			while processedDay != newestDay:
				stringDay=strDay(processedDay)
				if stringDay in self.dividendData[s]:
					dividend=self.dividendData[s][stringDay]
					yeld=dividend/(path[processedDay].amount*path[processedDay].basePrice)
					totalYeld+=yeld
				processedDay+=datetime.timedelta(1)
			prettyYeld=round(totalYeld,3)
			if self.db[s].etf == False:
				prettyYeld/=100
			self.db[s].yeld=prettyYeld
	
	def __init__(self):
		self.depositsData=[0]
		self.dividendData=[0]
		
	def loadDeposits(self,path):
		try:
			with open(path,'r') as file:
				self.depositsData=json.load(file)
		except FileNotFoundError:
			print(f'Cannot find file {path}')
			self.dividendData={}
			
	def loadDividends(self,path):
		try:
			with open(path,'r') as file:
				self.dividendData=json.load(file)
		except FileNotFoundError:
			print(f'Cannot find file {path}')
			self.dividendData={}
			
	def depositGraph(self):
		from moneyChamber.profitLossGraph import optimizeData
		import numpy as np
		
		def addDeposits():
			deposits=self.ordersData
			for day in self.totalPortfolio:
				total=self.totalPortfolio[day]
				if day in deposits:
					total+=deposits[day]
				print(total)
				
	def finaliseData(self):
		for stock in self.db:
			self.addPrices(stock)
		self.updateTotalPortfolio()
			
	def graph(self,style='armyBlue'):
		self.finaliseData()
		if not self.db:
			print('Load statement first')
			sys.exit()
		from moneyChamber.profitLossGraph import optimizeData
		import numpy as np
		dayValues=[v for v in self.totalPortfolio.values()]
		profit,loss,normal=optimizeData(dayValues)
		cStyles={'armyBlue':['#92C099','#C54E59','#304154'],
		'darkGreen':['#92C099','#C54E59','#154F55']
		}
		def dividendGraph():
			dividendPlotData=[]
			for day in self.totalDividendsDict.keys():
				for _ in range(int(multiplierV2+1)):
					dividendPlotData.append(self.totalDividendsDict[day])
			return dividendPlotData

		def showMonths():
			#list with first day of month index N
			fDayPositions=[]
			pDates=list(self.totalPortfolio.keys())
			for day in range(len(pDates)):
				if pDates[day][8:10]=='01':
					fDayPositions.append(day)
			fDayPositionsX=[v*multiplierV2 for v in fDayPositions]
			for n in fDayPositionsX:
				self.plt.axvline(n,color='white',alpha=0.1)
				
		def showYears():	
			nYPositions={}
			pDates=list(self.totalPortfolio.keys())
			savedYear=pDates[0][0:4]
			y=min(loss)-5
			for d in range(len(pDates)):
				if pDates[d][0:4]!=savedYear:
					savedYear=pDates[d][0:4]
					nYPositions[savedYear]=d
			for year in nYPositions.keys():
				x=nYPositions[year]*multiplierV2
				self.plt.axvline(x,color='white',alpha=0.5)
				self.plt.annotate(year,xy=(x+200,y))

		def prettyGraph():
			bgColor=cStyles[style][2]
			self.plt.rcParams['axes.facecolor']=bgColor
			self.plt.rcParams['axes.edgecolor']=bgColor
			self.plt.rcParams['figure.facecolor']=bgColor
			self.plt.rcParams['figure.edgecolor']=bgColor
			self.plt.rcParams['savefig.facecolor']=bgColor
			self.plt.rcParams['savefig.edgecolor']=bgColor
			self.plt.rcParams['text.color']='white'
			self.plt.rcParams['xtick.color']=bgColor
			self.plt.rcParams['ytick.color']='white'
			self.plt.rcParams['patch.edgecolor']='red'
			self.plt.rcParams['legend.loc']='lower left'
			self.plt.rcParams.update
		
		prettyGraph()
		self.plt.plot(profit,linewidth=2,color=cStyles[style][0],label='Profit')
		self.plt.plot(loss,linewidth=2,color=cStyles[style][1],label='Loss')
		self.plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='on', labelleft='on')
		multiplierV2=len(profit)/len(list(self.totalPortfolio.keys()))
		showMonths()
		showYears()
		dividends=dividendGraph()
		
		shortenDivX=len(dividends)-len(normal)
		dividends=dividends[shortenDivX:]
		dividendsX=np.arange(0,len(dividends),1)
		divPillow=[normal[i]-dividends[i] for i in range(len(profit))]
		normal[0]=0
		divPillow[0]=0
		self.plt.fill_between(dividendsX,normal,divPillow,color='white',alpha=0.05)
		self.plt.plot(divPillow,alpha=0.3, color='white',label='Dividends')
		self.plt.legend()
		self.plt.show()
	
	def createOrders(self):
		""" Create orders data from statement """
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
	
	def loadOrders(self,path):
		with open(path,'r') as file:
			self.ordersData=json.load(file)
		
	def updateTotalPortfolio(self):
		totalDeposits=0
		totalDividends=0
		for day in range((today-self.oldestDay).days):
			stringDay=strDay(self.oldestDay+datetime.timedelta(day))
			processedDay=(self.oldestDay+datetime.timedelta(day))
			totalForDay=0
			if stringDay in self.depositsData:
					totalDeposits+=self.depositsData[stringDay]
			for stockName in self.db:
				if processedDay in self.db[stockName].history:
					totalForDay+=self.db[stockName].history[processedDay].profit
				if stockName in self.dividendData:
					if stringDay in self.dividendData[stockName]:
						totalDividends+=self.dividendData[stockName][stringDay]
			self.totalPortfolio[stringDay]=totalForDay
			self.totalDividendsDict[stringDay]=totalDividends


	class Stock:
		__etfs__=['VUKE','VMID']
		def __init__ (self,l):
			
			self.date=self.processDate(l)
			self.buySell=l[3]
			self.amount=float(l[4])
			self.name=l[5]
			self.price=float(l[6])
			buyRange=(today-self.date).days
			self.history={(self.date+datetime.timedelta(d)):0 for d in range(buyRange)}
			
			self.updateETF()
			self.dividendTotal=0

		def processDate(self,l):
			return datetime.datetime.strptime(l[2],'%Y.%m.%d %H:%M').date()

		def updateETF(self):
			if self.name in self.__etfs__:
				self.etf=True
			else:
				self.etf=False
				self.price/=100

	def loadStatement(self,url):
		try:
			data=open(os.path.join(os.path.dirname(__file__),url),'r')
			result = [l.split('\t') for l in data]
		except FileNotFoundError:
			print(f'Cannot find {url}')
			sys.exit()
		data
		
		for d in result:
			self.db[d[5]]=self.Stock(d)
		self.ordersData=self.createOrders()
		self.oldestDay=min([self.db[stock].date for stock in self.db])
		

	def addPrices(self,stockName):
		class Day:
			def __init__(self,basePrice,amount,stockPrice,etf,dividend,deposits):
				if etf == False:
					stockPrice/=100
					basePrice/=100
				self.profit=round(((stockPrice-basePrice)*amount)+dividend,3)
				self.amount=amount
				self.stockPrice=stockPrice
				self.basePrice=basePrice
				self.dividendPaid=dividend
				self.totalDeposits=deposits
		
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
				except :
					print('Connection error')
					sys.exit()
			path=os.path.join(os.path.dirname(__file__),f"pickle/{stockName}.pickle")
			if stockName == "BT":
				stockName+=".A"
			try:
				res=pickle.load(open(path,'rb'))
				if todayUnixTime - os.path.getmtime(path) > 86400:
					res=downloadFreshStockData()
					print(f"Old data for {stockName}, dowloaded new one")
					pickle.dump(res,open(path,'wb'))
			except (FileNotFoundError):
				res = downloadFreshStockData()
				print("Downloaded "+str(stockName))
				pickle.dump(res,open(path,'wb'))
			return res
			
		def newBasePrice():
			if day != firstDay:
				bfAmount=amount
				newAmount,newPrice=self.ordersData[stockName][stringDay]
				bfPrice=basePrice
				totalBefore=bfAmount*bfPrice
				totalNew=newAmount*newPrice
				totalAmount=bfAmount+newAmount
				newBasePrice=(totalBefore+totalNew)/totalAmount
				return round(newBasePrice,3),totalAmount
			return basePrice,amount
		
		totalStockDividends=0
		priceData=oneTimeConnection()
		stockPrice=0
		firstDay=self.db[stockName].date
		strFirstDay=strDay(firstDay)
		amount=float(self.ordersData[stockName][strFirstDay][0])
		basePrice=float(self.ordersData[stockName][strFirstDay][1])
		etf=self.db[stockName].etf
		for day in self.db[stockName].history.keys():
			stringDay=strDay(day)

			# add dividends 
			if stockName in self.dividendData:
				if stringDay in self.dividendData[stockName]:
					totalStockDividends+=self.dividendData[stockName][stringDay]
					self.db[stockName].dividendTotal+=totalStockDividends
			#count new base price
			if stringDay in self.ordersData[stockName]:
				basePrice,amount=newBasePrice()
			#update stock price if markets were opened
			if stringDay in priceData:
				stockPrice=float(priceData[stringDay]['close'])
			self.db[stockName].history[day]=Day(basePrice,amount,stockPrice,etf,totalStockDividends,0)
				

pass
