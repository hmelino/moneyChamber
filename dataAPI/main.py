import downloadData
import emailData
from emailData import *
import emailObject
from emailObject import *
from downloadData import *
import json
import historyData
from historyData import *
import functionsLibrary
from functionsLibrary import *
import graph
from graph import *
import datetime

start = time.time()
mainArray=[]
dateArray=[]
floatArray=[]


def createGraphData(selectedStock):
	#selectedStock
	s = selectedStock
	#create Stock Class
	mainArray=emailObject.createStockClass()
	#choose stock for processing
	selctedTicker = mainArray[s].ticker
	priceBoughtAt = mainArray[s].price
	#find bough at date 
	boughtAt = mainArray[s].date
	#dowload history data from internet
	dataJSON=downloadData.oneTimeConnection(selctedTicker)
	#create array of prices
	dateArray=[(historyData.historyPrices(boughtAt,dataJSON))][0]
	#remove weekends
	dateArray=historyData.removeWeekends(dateArray)
	#replace bank holiday
	dateArray=historyData.updateBankHolidayDays(dateArray)
	#create oldest Date
	oldestDay=functionsLibrary.startDate(mainArray)
	#fill array with zeros before buy
	functionsLibrary.beforeBuyDays(oldestDay,boughtAt,dateArray)
	floatArray=(functionsLibrary.createFloatArray(s,dateArray,mainArray,priceBoughtAt))
	graph.createGraph(floatArray)
	
	
	
	
	
createGraphData(9)
end = time.time()
print(end-start)







