import requests
from sensData import apiKey
import datetime
import sys


def historyPerformance(stockName,firstDay):
	priceData=None
	today=datetime.datetime.today().date()
	dateRange=(today-firstDay).days

	class Day:
		def __init__(self,stockPrice,dividendPaid,basePrice):
			self.stockPrice=stockPrice
			self.dividendPaid=dividendPaid
			self.basePrice=basePrice
	
	def oneTimeConnection(stockName):
		if stockName == "BT":
			stockName+=".A"
		try:
			res = requests.get(f'https://api.worldtradingdata.com/api/v1/history?symbol={stockName}.L&sort=newest&api_token={apiKey}').json()
			print("Dowloaded "+str(stockName))
			return res
		except requests.exceptions.ConnectionError:
			print('You are offline')
			sys.exit()

	def processPastPerformance(firstDay=firstDay):
		def strDay(day):
			return datetime.datetime.strftime(day,'%Y-%m-%d')

		def pastDay(dayN,data=priceData['history'],firstDay=firstDay):
			sDay=strDay(firstDay+datetime.timedelta(dayN))
			if sDay in data:
				stockPrice=data[sDay]['close']
			else:
			# if markets were closed on searched day, search day before
				foundDay=False
				while foundDay is False:
					if sDay in data:
						stockPrice=data[sDay]['close']
						foundDay=True
					else:
						dayN-=1
			return Day(stockPrice,0,0)

		return {strDay(firstDay+datetime.timedelta(dayN)):pastDay(dayN) for dayN in range(dateRange)}


	priceData=oneTimeConnection(stockName)
	return processPastPerformance(firstDay)

p=historyPerformance('VUKE',datetime.datetime(2019,2,3).date())
pass
	



	
		

	
	
