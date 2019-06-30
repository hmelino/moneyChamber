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
import datetime
import operator
import matplotlib
import matplotlib.pyplot as plt


vuki={'2019-06-25':7,'2019-05-14':5,'2019-05-09':2,'2019-05-08':3,'2019-04-29':2}

def createPreviousBasePrice(historyDic,selectedStock):
	basePrice=float(mainStockArray[selectedStock].price)
	lenOfBuys=int((len(vuki)))
	for n in historyDic:
		previousDay=n-datetime.timedelta(1)
		price=historyDic[n][0]
		amount=int(historyDic[n][1])
		#how many times bough this stock
		if str(n) in vuki and lenOfBuys>1:
		  m = basePrice*amount
		  o = amount-(historyDic[previousDay][1])
		  l = (float(historyDic[n][0])/100)*o
		  k =m-l
		  basePrice=round(k/historyDic[previousDay][1],2)
		  historyDic[n][2]=basePrice
		  historyDic.update
		  # to protect from out of range 
		  lenOfBuys=lenOfBuys-1
		else:
		  historyDic[n][2]=basePrice
	
		  
				
				  
		




start = time.time()
def createData(selectedStock):
	stockTicker=mainStockArray[selectedStock].ticker
	#oldest day of buy
	oldestDay=functionsLibrary.startDate(mainStockArray)
	firstDay=mainStockArray[selectedStock].date
	
	#dowload all stock data avaiable
	jsonData=downloadData.oneTimeConnection(stockTicker)
	# define date now
	dateNow=datetime.datetime.today().date()
	
	howManyDays=(dateNow-firstDay)
	
	ownershipPeriod=howManyDays.days
	
	# create countable unit of 1 day
	oneDay=datetime.timedelta(1)
	
	print("You held "+str(stockTicker)+"for "+str(ownershipPeriod)+" days")
	
	#count total Amount owning by today 
	totalAmountToday=0
	for n in vuki.values():
		totalAmountToday=totalAmountToday+int(n)
	amount=totalAmountToday
	
	
	stockTotalTotal=totalAmountToday*mainStockArray[selectedStock].price
	
	
	priceDic={}
	
	
	# create dic of prices based on how long I owned them
	#demDate[date]=price 
	priceDicValue=0
	boughtAt=0
	for n in range(int(ownershipPeriod)+1):
		demDate = dateNow-datetime.timedelta(n)
		if str(demDate) in jsonData['Time Series (Daily)']:
		  priceDicValue = float(jsonData['Time Series (Daily)'][str(demDate)]['4. close'])
		  priceDic[demDate]=priceDicValue
		  if demDate in vuki:
		    firstlart=float(vuki[demDate])/totalAmountToday
		else:
			#if date doesnt exist, put previous value
			priceDic[demDate]=priceDicValue
	
	#fix first 1 or 2 days with 0 prices
	for n in priceDic:
	  if priceDic[n]!=0 and priceDic[n+oneDay]==0:
	    if priceDic[n+oneDay*2]==0:
	      priceDic[n+oneDay*2]=priceDic[n]
	      priceDic[n+oneDay]=priceDic[n]
	    else:priceDic[n+oneDay]=priceDic[n]
	
	

	
	
#create floatDic from priceDic
	floatDic={}
	boughtAt = mainStockArray[selectedStock].price
	boughtWhen = mainStockArray[selectedStock].date
	
	
		
	
	for n in priceDic:
		if str(n) in vuki:
			amount=amount-int((vuki[str(n)]))
			floatDic[n]=((priceDic[n]-float(boughtAt))*float(amount))/100
		else:
			floatDic[n]=((priceDic[n]-float(boughtAt))*float(amount))/100
	
	#create history dictionary
	historyDic={}
	amount = totalAmountToday
	baseprice=mainStockArray[selectedStock].price
	
	for n in priceDic:
		if str(n) in vuki:
			historyDic[n]=[float(priceDic[n]),int(amount),float(baseprice)]
			amount=amount-vuki[str(n)]
			

		else:
			historyDic[n]=[float(priceDic[n]),int(amount),float(baseprice)]
		
	
				
				
			
	createPreviousBasePrice(historyDic,selectedStock)

	
	
	#turn dictionary into array 
	floatArray=[]
	for n in floatDic.values():
		floatArray.append(float(n)/100)
		
	#save dictiinary to mainArray
	mainStockArray[selectedStock].arrej=floatDic
	
	#create graph
	plt.plot(floatArray)
	plt.axhline(0, color='lightseagreen')
	plt.show()
	
	
	print(floatDic)
	return floatDic
	
	
	
	


dezArray=[]
mainStockArray=emailObject.createStockClass()
createData(0)

end = time.time()
print(end-start)


		





