from emailObject import processMonthlyStatement
from realTimeData import getRealTimeData
from buyInfoParse import parseBuyInfoV4, parseDividendV2
from historyProfit import historyProfit
from historyDic import stockFloat,HistoryPrice
from addTodaysPrices import addTodaysPrices
from etfCheck import etfCheck
from saveFile import saveMsArray
from graphFunctions import plotGraph
from mainStockArray import updateStockAmountTotal
import sys

	

oldestDay=None
msArray = processMonthlyStatement()
etfCheck(msArray)

def findOldestDay(msArray):
	import datetime
	oldestDay=datetime.datetime.today().date()
	for stock in msArray:
		day=msArray[stock].firstBuy.date()
		if day < oldestDay:
			oldestDay=day
	return oldestDay

portfolioAttributes=None
	
	
parseBuyInfoV4(msArray,"buyInfo.py")
parseBuyInfoV4(msArray,"dividendInfo.py")
totalFloat=historyProfit(msArray,stockFloat)
addTodaysPrices(msArray)
plotGraph(totalFloat)
updateStockAmountTotal(msArray)
saveMsArray(msArray)

#def totalDividendPaid():
	

	
def everyDayInYear(day:int):
	import datetime
	return (datetime.datetime.today().date()-datetime.timedelta(day))
	

#totalDividendPaid()
