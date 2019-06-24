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
import operator


start = time.time()


def createGraphData(selectedStock):
	startt=time.time()
	floatArray = []
	newFloatAtray = []
	newFloatAtray.clear
	#selectedStock
	s = selectedStock
	#create Stock Class
	#choose stock for processing
	selctedTicker = mainStockArray[s].ticker
	print("processing ..."+str(mainStockArray[s].ticker))
	priceBoughtAt = mainStockArray[s].price
	#find bough at date 
	boughtAt = mainStockArray[s].date
	#dowload history data from internet
	dataJSON=downloadData.oneTimeConnection(selctedTicker)
	
	#print(dataJSON)
	#create oldest Date
	keys=(dataJSON['Time Series (Daily)'].keys())
	dividend = []
	print("keys len is "+str(len(keys)))
			
		
		
	oldestDay=functionsLibrary.startDate(mainStockArray)
	
	#create array of prices
	dateArray=historyData.historyPrices(boughtAt,dataJSON)
	#remove weekends
	dateArray=historyData.removeWeekends(dateArray)
	#replace bank holiday
	dateArray=historyData.updateBankHolidayDays(dateArray)
	#print(dateArray)

	#fill array with zeros before buy
	functionsLibrary.beforeBuyDays(oldestDay,boughtAt,dateArray)
	#print(dateArray)
	#functionsLibrary.priceAnomaly(dateArray)
	functionsLibrary.priceCheck(dateArray)
	#print(dateArray)
	floatArray=functionsLibrary.createFloatArray(s,dateArray,mainStockArray,priceBoughtAt,newFloatAtray)
	endd= time.time()
	print("took "+str(endd-startt)+"sec to process")
	return floatArray
	
	

	
	
dezArray=[]
mainStockArray=emailObject.createStockClass()
for n in range(9,13):
	data = createGraphData(n)
	dezArray.append(data)
	


totalArray=functionsLibrary.createSumFloatArray(dezArray)
print(totalArray)
print(len(totalArray))
print(de)






	
#print(totalArray)
graph.createGraph(totalArray)

end = time.time()
print(end-start)


		





