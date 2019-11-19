import datetime
import time
import re
import webDataResult3
import emailData
from emailData import *
from webDataResult3 import *
import json


start = time.time()
arrayOfArrays =[]
dateArray = []
startDateofArray = datetime.date(2019,2,5)
	#index num of week
print("dayOfWeek")
print(startDateofArray.weekday())
startWeekIndex= startDateofArray.weekday()




boughtAtDate = emailData.demData[1:]

def historyPrices (givenString):
	howManyStocks = boughtAtDate.count
	print(howManyStocks)
	print("------")
	arrayOfArrays.append(dateArray)
	datenow = datetime.date.today()
	
	
	beforeBuyDays = (datenow-startDateofArray).days
	#for n in range(beforeBuyDays):
		#dateArray.append(0)
	#turn string into date
	boughAt = givenString[1]
	dhdj = boughAt.split()
	leCode = datetime.datetime.strptime(str(dhdj[0]),"%Y.%m.%d").date()
	print(leCode)
	opo = re.sub("[',:.']"," ",str(dhdj))
	lol = opo.split()
	year=(lol[1])
	month=(lol[2])
	day=(lol[3])
	toProcess=datetime.date(int(year),int(month),int(day))
	howManyDays=(datenow-leCode).days
	print(howManyDays)
	
	for n in range(howManyDays):
		duj = datetime.timedelta(1+n)
		pastDate = str(leCode-duj)
		if pastDate in webDataResult3.demData['Time Series (Daily)']:
			dateArray.append(webDataResult3.demData['Time Series (Daily)'][str(pastDate)]['4. close'])
		else: 
			dateArray.append(0)
			#print("Nah")
			pass
	
	end =time.time()
	print(end-start)
	print(arrayOfArrays)
	print("starting func")
	
	for n in enumerate(dateArray):
		print(n)
		
		
	
def removeWeekends (indexOfStartDate):
	print("RemoveWeekends")
	weeksAmount = (len(dateArray)/7)
	print(weeksAmount)
	numIndex = 0
	print("*******")
	print(dateArray)
	#print(dateArray[160])
	for n in range(7):
		#print(dateArray[numIndex])
		del dateArray[numIndex]
		del dateArray[numIndex]
		#print(dateArray[numIndex+1])
		numIndex=numIndex+5
	print(dateArray)
		
	
	
historyPrices(boughtAtDate)
removeWeekends(startWeekIndex)





	
