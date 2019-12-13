from sensData import realTwebsite
import requests
import datetime
from historyDic import HistoryPrice
import sys
import pickle

class RTData:
	def __init__(self,data,date):
		self.data=data
		self.date=date
		
def getJsonData():
	try:
		print("Downloading Real Time Data")
		jsonData=requests.get(realTwebsite).json()
		print(f"Data as of {datetime.datetime.today().strftime('%d-%m-%Y , %H:%M')}")
		return jsonData
	except :
		data=pickle.load(open("pickle/realTData.pickle","rb"))
		print(f"loading realTimeData {data.date.strftime('%d-%m-%Y')}")
		print(f"Real time data as of {data.date.strftime('%H:%M')}")
		return data.data
	if not jsonData:
		print("You are offline")
		print("No data saved")
		sys.exit()

def savejsonData(jsonData):
	file=RTData(jsonData,datetime.datetime.today())
	pickle.dump(file,open("pickle/realTData.pickle","wb"))




#main function
def addTodaysPrices(msArray):
	jsonData=getJsonData()
	savejsonData(jsonData)
	
	namesArray=[f for f in msArray]
	resultDicV2={jsonData[q]['name']:jsonData[q]['price']['buy'] for q in range(len(jsonData)) if jsonData[q]['name'] in namesArray and jsonData[q]['margin']==1}

	today=datetime.datetime.today().strftime("%Y-%m-%d")
	yesterday=(datetime.datetime.today()-datetime.timedelta(1)).strftime("%Y-%m-%d")
	for stock in resultDicV2:
		if msArray[stock].etf == False:
			resultDicV2[stock]/=100
		if yesterday not in msArray[stock].historyDic:
			dayBeforeYesterday=(datetime.datetime.today()-datetime.timedelta(2)).strftime("%Y-%m-%d")
			msArray[stock].historyDic[yesterday]=msArray[stock].historyDic[dayBeforeYesterday]
		yesterdayData=msArray[stock].historyDic[yesterday]
		todaysPrice=resultDicV2[stock]
		todaysProfit=(todaysPrice-yesterdayData.basePrice)*yesterdayData.amount
		msArray[stock].historyDic[today]=HistoryPrice(yesterdayData.basePrice,yesterdayData.amount,todaysProfit,yesterdayData.dividends)
	return msArray