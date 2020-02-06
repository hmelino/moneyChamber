import requests

import datetime
import pickle
import sys

	

importApiKey()
today=datetime.datetime.today().date()
dbYesterday=today-datetime.timedelta(2)
class Day:
	def __init__(self,stockPrice,amount,basePrice,dividends):
		self.stockPrice=stockPrice
		self.amount=amount
		self.basePrice=basePrice
		self.dividends=dividends
		
def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')
	

		
randomDate=datetime.datetime(2019,2,5).date()




def processPastPerformance(firstDay,stockName,hDB):
	stockPrice=0
	def oneTimeConnection(stockName=stockName):
		if stockName == "BT":
			stockName+=".A"
		try:
			res=pickle.load(open(f"pickle/{stockName}.pickle","rb"))
			res[strDay(dbYesterday)]
			print(f"Loaded {stockName}")
		except (FileNotFoundError,KeyError):
			res = requests.get(f'https://api.worldtradingdata.com/api/v1/history?symbol={stockName}.L&sort=newest&api_token={apiKey}').json()['history']
			print("Dowloaded "+str(stockName))
			pickle.dump(res,open(f"pickle/{stockName}.pickle",'wb'))
		return res

	def pastDay(n,historyData,firstDay,stockPrice=stockPrice):
		day=firstDay+datetime.timedelta(n)
		sDay=strDay(day)
		print(sDay)
		if sDay in historyData:
			stockPrice=historyData[sDay]['close']
			print(stockPrice)
		return Day(stockPrice,0,0,0)

	def pastDayV2():
		for 

	today=datetime.datetime.today().date()
	history=oneTimeConnection()
	d={strDay(firstDay+datetime.timedelta(d)):pastDay(d,history,firstDay) for d in range((today-firstDay).days)}
	return d

	

	
	
w=processPastPerformance(randomDate,'VUKE')
pass
	
	
