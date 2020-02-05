import requests
from sensData import apiKey
import datetime
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

randomDate=datetime.datetime(2019,2,5).date()
def strDay(day):
	return datetime.datetime.strftime(day,'%Y-%m-%d')

def pastDay(n,historyData,firstDay):
	day=firstDay+datetime.timedelta(n)
	return strDay(day)


def processPastPerformance(data,firstDay):
	today=datetime.datetime.today().date()
	history=data['history']
	d=[pastDay(d,history,firstDay) for d in range((today-firstDay).days)]
	return d
w=processPastPerformance(oneTimeConnection("VUKE"),randomDate)
	
	
