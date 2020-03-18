import datetime
import pickle
import requests
import sys
import os
import time
import json
		
today=datetime.datetime.today().date()

class Portfolio:
	import matplotlib.pyplot
	
	plt=matplotlib.pyplot
	dayTotals={}
	oldestDay=None
	db={}
	profit=0
	totalDividendsDict={}
	apiKey=None

	def strDay(self,day):
		return datetime.datetime.strftime(day,'%Y-%m-%d')
		
	def fullCWD(self):
		cwd=os.getcwd()
		if '//' in cwd:
			return f'{cwd}//'
		return f'{cwd}/'

	def finaliseData(self):
		from moneyChamber.prices import addPrices
		apiKey=self.apiKey
		#Download and process stock prices
		for stock in self.db:
			addPrices(self,stock,apiKey)
		#Count daily totals for graph
		self.updateDayTotals()

	def showGraph(self):
		from moneyChamber.graph import showGraphV2
		showGraphV2(self)

	def showDepositGraph(self):
		from moneyChamber.depositGraph import showDepositGraph
		showDepositGraph(self)
		
	def __init__(self,statementPath):
		self.cwd=self.fullCWD()
		self.depositsData=[0]
		self.dividendData=[0]
		self.loadStatement(statementPath)
		
		
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
			d=list(self.dayTotals.keys())[-1]
			return (datetime.datetime.strptime(d,'%Y-%m-%d')).date()
		
		newestDay=getNewestDay()
		day=newestDay

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
				stringDay=self.strDay(processedDay)
				if stringDay in self.dividendData[s]:
					dividend=self.dividendData[s][stringDay]
					yeld=dividend/(path[processedDay].amount*path[processedDay].basePrice)
					totalYeld+=yeld
				processedDay+=datetime.timedelta(1)
			prettyYeld=round(totalYeld,3)
			if self.db[s].etf == False:
				prettyYeld/=100
			self.db[s].yeld=prettyYeld
		
	def loadDeposits(self,filename):
		path=self.cwd+filename
		try:
			with open(path,'r') as file:
				self.depositsData=json.load(file)
		except FileNotFoundError:
			print(f'Cannot find file {path}')
			self.dividendData={}
			
	def loadDividends(self,filename):
		path=self.cwd+filename
		try:
			with open(path,'r') as file:
				self.dividendData=json.load(file)
		except FileNotFoundError:
			print(f'Cannot find file {path}')
			self.dividendData={}

	def createOrders(self):
		""" Create orders data from statement """
		d=self.db
		data={d[s].name:{self.strDay(d[s].date):[d[s].amount,d[s].price]} for s in d}

		#adjust prices for non ETF
		for stock in data.keys():
			etfs=self.Stock.__etfs__
			if stock not in etfs:
				for date in data[stock].keys():
					secondPart=data[stock][date]
					secondPart[1]*=100
		return data
	
	def loadOrders(self,filename):
		path=self.cwd+filename
		try:
			with open(path,'r') as file:
				self.ordersData=json.load(file)
		except FileNotFoundError:
			print(f'Cannot find {filename}')
			print(f'Your working directory is {os.getcwd()}')
			sys.exit()
		
	def updateDayTotals(self):
		totalDeposits=0
		totalDividends=0
		for day in range((today-self.oldestDay).days):
			stringDay=self.strDay(self.oldestDay+datetime.timedelta(day))
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
			self.dayTotals[stringDay]=totalForDay
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

	def loadStatement(self,filename):
		def loadStatementFile(filename):
			
			path=self.cwd+filename
			try:
				data=open(path,'r')
				return [l.split('\t') for l in data]
			except FileNotFoundError:
				print(f'Cannot find {url}')
				print(f'Your working directory is {os.getcwd()}')
				sys.exit()

		statementFile=loadStatementFile(filename)
		# process each line in statement as separate stock 
		for d in statementFile:
			self.db[d[5]]=self.Stock(d)
		self.ordersData=self.createOrders()
		self.oldestDay=min([self.db[stock].date for stock in self.db])		

pass
