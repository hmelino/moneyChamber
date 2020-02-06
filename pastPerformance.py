import requests
from sensData import apiKey
import datetime
import pickle
import sys
today=datetime.datetime.today().date()
dbYesterday=today-datetime.timedelta(2)

			
def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')
	
def oneTimeConnection(stockName):
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
		
randomDate=datetime.datetime(2019,2,5).date()

def pastDay(n,historyData,firstDay):
	day=firstDay+datetime.timedelta(n)
	return strDay(day)

def processPastPerformance(data,firstDay):
	today=datetime.datetime.today().date()
	history=data
	d=[pastDay(d,history,firstDay) for d in range((today-firstDay).days)]
	return d
	
w=processPastPerformance(oneTimeConnection("VUKE"),randomDate)
	
	
