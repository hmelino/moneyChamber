import datetime
import pickle
from pastPerformance import oneTimeConnection
today=datetime.datetime.today().date()

class MoneyChamber:
	db={}
	def __init__(self):
		self.loadStatement('statementV2.txt')
		self.addPastPerformance()
		
	class Stock:
		def __init__ (self,l):
			self.date=self.processDate(l)
			self.buySell=l[3]
			self.amount=l[4]
			self.name=l[5]
			self.price=l[6]
			
		def processDate(self,l):
			return datetime.datetime.strptime(l[2],'%Y.%m.%d %H:%M')
			
	def loadStatement(self,url):
		try:
			self.db=pickle.load(open("db.pickle","rb"))
		except FileNotFoundError:
			data=open(url,'r').readlines()
			result = [l.split('\t') for l in data]
			for d in result:
				self.db[d[5]]=self.Stock(d)
			pickle.dump(data,open("db.pickle","wb"))
			
	def addPastPerformance(self):
		for stock in MoneyChamber.db.keys():
			print(stock)
			pPerformance=oneTimeConnection(stock)
			
o=MoneyChamber()
pass
