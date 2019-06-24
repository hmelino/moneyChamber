import datetime
import time
import re
import json

#boughtDate=datetime.strftime("2019-04-29","%Y-%m-%d")
#boughtDaate=datetime.datetime.strptime(str(2019-04-29),'%Y-%m-%d')
boughDate=datetime.datetime.strptime("2019.04.29","%Y.%m.%d").date()

#arrayOfArrays =[]
#dateArray = []
#divArrayAmount = []
#divArrayDate = []

startDateofArray = datetime.date(2019,2,5)
startWeekIndex= startDateofArray.weekday()





def historyPrices (boughtAt,downloadedData):
	dateArray=[]
	if 'Note' in downloadedData:
		print("wrong data")
		print(downloadedData)
	else:pass
	datenow = datetime.date.today()
	beforeBuyDays = (datenow-startDateofArray).days
	howManyDays=(datenow-boughtAt).days
	print(str(howManyDays)+" days between today and stock bought")
	for n in range(howManyDays):
		duj = datetime.timedelta(1-n)
		pastDate = str(boughtAt-duj)
		if pastDate in downloadedData['Time Series (Daily)']:
			dateArray.append(downloadedData['Time Series (Daily)'][str(pastDate)]['4. close'])
		else: 
			dateArray.append(0)
			pass
			
	
			
	return dateArray
	 
	
	
		
	
def removeWeekends (array):
	weeksAmount = (len(array)/7)
	numIndex = startWeekIndex-1
	for n in range(7):
		del array[numIndex]
		del array[numIndex]
		numIndex=numIndex+5
	return array
	
def updateBankHolidayDays(array):
	indexNum = 0
	for n in array:
		if n == 0:
			array[indexNum]=array[indexNum-1]
			indexNum=indexNum+1
		else:
			indexNum=indexNum+1
	return array

