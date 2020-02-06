import datetime
import pickle
import requests
import sys

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

today=datetime.datetime.today().date()
def strDay(day):
		return datetime.datetime.strftime(day,'%Y-%m-%d')

class MoneyChamber:
	totalPortfolio={}
	oldestDay=None
	db={}
	def __init__(self):
		self.loadStatement('statementV2.txt')
		self.oldestDay=min([self.db[stock].date for stock in self.db])
		for stock in self.db:
			self.addPrices(stock)
		self.updateTotalPortfolio()
		
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
		def oneTimeConnection(stockName=stockName):
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
		
		priceData=oneTimeConnection()

		class Day:
			def __init__(self,basePrice,dividend,amount,stockPrice):
				self.dividend=dividend
				self.profit=(stockPrice-basePrice)*amount

		stockPrice=0
		amount=float(self.db[stockName].amount)
		basePrice=float(self.db[stockName].price)
		for day in self.db[stockName].history.keys():
			if day in priceData:
				stockPrice=float(priceData[day]['close'])
				if self.db[stockName].etf is False:
					stockPrice/=100
			self.db[stockName].history[day]=Day(basePrice,0,amount,stockPrice)
				

o=MoneyChamber()
pass
