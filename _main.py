from msArrayObject import getMsArray
from realTimeData import getRealTimeData
from processStatementInfo import processStatementV4
from historyProfit import historyProfit
from historyDic import stockFloat,HistoryPrice
from addTodaysPrices import addTodaysPrices
from saveFile import saveMsArray
from graphFunctions import plotGraph
from mainStockArray import updateStockAmountTotal
import sys

msArray = getMsArray()

def findOldestDay(msArray):
	import datetime
	oldestDay=datetime.datetime.today().date()
	for stock in msArray:
		day=msArray[stock].firstBuy.date()
		if day < oldestDay:
			oldestDay=day
	return oldestDay


	
	
processStatementV4(msArray,"buyInfo.py")
processStatementV4(msArray,"dividendInfo.py")
totalFloat=historyProfit(msArray,stockFloat)
addTodaysPrices(msArray)
plotGraph(totalFloat)
updateStockAmountTotal(msArray)
saveMsArray(msArray)

def totalDividendPaid(oldestDay):
	import datetime
	totalDiv=0
	timeRange=datetime.datetime.today().date()-oldestDay
	for day in range(timeRange.days):
		pDay=oldestDay+datetime.timedelta(day)
		
		for stock in msArray:
			if pDay in msArray[stock].dividendInfo:
				totalDiv+=mainStockArray[stock].dividendInfo
	return totalDiv
				
	

	
def everyDayInYear(day:int):
	import datetime
	return (datetime.datetime.today().date()-datetime.timedelta(day))
	
oDay=findOldestDay(msArray)
o=totalDividendPaid(oDay)
#totalDividendPaid()
