import datetime
import pickle
import requests
import sys
from matplotlib import pyplot as plt

def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')
		
today=datetime.datetime.today().date()

class MoneyChamber:
	totalPortfolio={}
	oldestDay=None
	db={}
	orders=None
	
	def __init__(self):
		self.loadStatement('statementV2.txt')
		self.orders=self.loadOrders()
		self.oldestDay=min([self.db[stock].date for stock in self.db])
		for stock in self.db:
			self.addPrices(stock)
		self.updateTotalPortfolio()
		plt.plot([v for v in self.totalPortfolio.values()])
		plt.show()
		
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
			from orders import data
			return data
			
		except ModuleNotFoundError:
			return createOrders()
			
		except ImportError:
			print('Create variable "data" inside of orders.py with all stock orders')
			
	def updateTotalPortfolio(self):
		for day in range((today-self.oldestDay.date()).days):
			stringDay=strDay(self.oldestDay+datetime.timedelta(day))
			totalForDay=0
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

		def processDate(self,l):
			return datetime.datetime.strptime(l[2],'%Y.%m.%d %H:%M')

		def updateETF(self):
			if self.name in self.__etfs__:
				self.etf=True
			else:
				self.etf=False
				self.price/=100

	def loadStatement(self,url):
		''' just for testing '''
		print('Created db')
		data=open(url,'r').readlines()
		result = [l.split('\t') for l in data]
		for d in result:
			MoneyChamber.db[d[5]]=self.Stock(d)
		'''
		try:
			self.db=pickle.load(open("db.pickle","rb"))
			print('Loaded')
		except FileNotFoundError:
			data=open(url,'r').readlines()
			result = [l.split('\t') for l in data]
			for d in result:
				MoneyChamber.db[d[5]]=self.Stock(d)
			pickle.dump(self.db,open("db.pickle","wb"))
		'''
	def addPrices(self,stockName):
		class Day:
			def __init__(self,basePrice,dividend,amount,stockPrice,etf):
				if etf == False:
					stockPrice/=100
					basePrice/=100
				self.dividend=dividend
				self.profit=round((stockPrice-basePrice)*amount,3)
				self.amount=amount
				self.stockPrice=stockPrice
				self.basePrice=basePrice
				#print(f'{stockName}|{stockPrice}|{basePrice}|')
		
		def oneTimeConnection(stockName=stockName):
			def importApiKey():
				try:
					from sensData import apiKey
					return apiKey
				except ModuleNotFoundError:
					print('Please create sensData.py file inside MoneyChamber folder')
					sys.exit()
				except ImportError:
					print("Please create variable 'apiKey=your_worldtradingdata.com_api_key' inside sensData.py")
					sys.exit()
			
			apiKey=importApiKey()
			dbYesterday=today-datetime.timedelta(2)
			if stockName == "BT":
				stockName+=".A"
			try:
				res=pickle.load(open(f"pickle/{stockName}.pickle","rb"))
				res[strDay(dbYesterday)]
				print(f"Loaded {stockName}")
			except (FileNotFoundError,KeyError):
				res = requests.get(f'https://api.worldtradingdata.com/api/v1/history?symbol={stockName}.L&sort=newest&api_token={apiKey}').json()
				res=res['history']
				print("Dowloaded "+str(stockName))
				pickle.dump(res,open(f"pickle/{stockName}.pickle",'wb'))
			return res
			
		def newBasePrice():
			if day != firstDay:
				bfAmount=amount
				newAmount,newPrice=orders[stockName][day]
				bfPrice=basePrice
				totalBefore=bfAmount*bfPrice
				totalNew=newAmount*newPrice
				totalAmount=bfAmount+newAmount
				newBasePrice=(totalBefore+totalNew)/totalAmount
				return round(newBasePrice,3),totalAmount
			return basePrice,amount
			
		priceData=oneTimeConnection()
		orders=self.orders
		stockPrice=0
		firstDay=strDay(self.db[stockName].date)
		amount=float(orders[stockName][firstDay][0])
		basePrice=float(orders[stockName][firstDay][1])
		etf=self.db[stockName].etf
		for day in self.db[stockName].history.keys():
			if day in orders[stockName]:
				basePrice,amount=newBasePrice()
				
			if day in priceData:
				stockPrice=float(priceData[day]['close'])
			
			self.db[stockName].history[day]=Day(basePrice,0,amount,stockPrice,etf)
				
o=MoneyChamber()
pass
