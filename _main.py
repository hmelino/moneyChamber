import traceback
traceback.print_exc()
from emailObject import getMsArray, saveMsArray , StockV2
from realTimeData import getRealTimeData
from processBuyStatement import processStatementV4
from historyProfit import historyProfit
from historyDic import stockFloat,HistoryPrice
from addTodaysPrices import addTodaysPrices
#from saveFile import saveMsArray
from graphFunctions import plotGraph
from mainStockArray import updateStockAmountTotal
import sys

msArray = getMsArray()

	
	
processStatementV4(msArray,"buyInfo.py")
processStatementV4(msArray,"dividendInfo.py")
totalFloat=historyProfit(msArray,stockFloat)
addTodaysPrices(msArray)
plotGraph(totalFloat)
updateStockAmountTotal(msArray)
saveMsArray(msArray)
#saveMsArray(msArray)


def totalDividendPaid(oldestDay):
	import datetime
	totalDiv=0
	timeRange=datetime.datetime.today().date()-oldestDay
	for day in range(timeRange.days):
		pDay=oldestDay+datetime.timedelta(day)
		
		for stock in msArray:
			if pDay in msArray[stock].dividendInfo:
				totalDiv+=msArray[stock].dividendInfo
	return totalDiv
				
	

	
def everyDayInYear(day:int):
	import datetime
	return (datetime.datetime.today().date()-datetime.timedelta(day)).days
	

o=totalDividendPaid(StockV2.oldestDay)
#totalDividendPaid()
o=0