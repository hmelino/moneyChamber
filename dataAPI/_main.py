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
import buyInfoParse
from buyInfoParse import *
import dividendInfo
from dividendInfo import *


vuki={'2019-06-25':7,'2019-05-14':5,'2019-05-09':2,'2019-05-08':3,'2019-04-29':2}


start = time.time()
def createData(selectedStock):
  transactionDic=mainStockArray[selectedStock].transactionDic
  stockTicker=mainStockArray[selectedStock].ticker
  
  
  
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
  for n in transactionDic.values():
    totalAmountToday=totalAmountToday+int(n)
  amount=totalAmountToday
  
  stockTotalTotal=totalAmountToday*mainStockArray[selectedStock].price
  
  priceDic=functionsLibrary.createPriceDic(ownershipPeriod,dateNow,jsonData,transactionDic)
  
  
  priceDic=functionsLibrary.fixZeroPriceDay(priceDic,oneDay)
  priceDic=functionsLibrary.fixPriceAnomalies(mainStockArray,priceDic,selectedStock)
  
  historyDic=functionsLibrary.createHistoryDic(totalAmountToday,mainStockArray,selectedStock,priceDic)
  # update previous base prices in History Dictionary
  historyDic=functionsLibrary.createPreviousBasePrice(historyDic,selectedStock,mainStockArray)
  
  
  #countFloats

  dateArray=functionsLibrary.dateArray(mainStockArray)

  # create floatArray from floatDic
  floatArray=functionsLibrary.floatArrayFromDic(historyDic,dateArray)
  
  
  
  #save dictiinary to mainArray
  #mainStockArray[selectedStock].arrej=floatDic
  
  #create graph
  #plt.plot(floatArray)
  #plt.axhline(0, color='lightseagreen')
  #plt.show()
  
  return floatArray
	
	
	
############################ start of program
dividendInfo=
buyInfo=buyInfoParse.parseBuyInfo()
mainStockArray=emailObject.createStockClass()
dictionary={}
for n in range(len(buyInfo)):
  mainStockArray[n].transactionDic=buyInfo[n]


mainStockArray=functionsLibrary.multipyETFprice(mainStockArray)
dateArray=functionsLibrary.dateArray(mainStockArray)
floatArray=[]
for n in range(14):
  o=createData(n)
  floatArray.append(o)

zfloat=[]
for day in range(len(floatArray[0])):
  data=0
  for array in floatArray:
    data=float(array[day])+data
  zfloat.append(data)


plt.plot(zfloat)
plt.axhline(0, color='lightseagreen')
plt.show()


end = time.time()
print(end-start)




		





