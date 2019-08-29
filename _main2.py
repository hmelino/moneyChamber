import emailObject
from emailObject import createStockClass
import downloadData
from downloadData import oneTimeConnection
import datetime
import realTimeData
from realTimeData import getRealTimeData
import buyInfoParse
from buyInfoParse import parseBuyInfoV3, parseDividendV2
import sys
import re
import ast
import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import functionsV2
from functionsV2 import updateStockTotalAmount
import indexFund
from indexFund import *
today = str(datetime.date.today())

timeStart=datetime.datetime.now()
def dateConvert(inputDate):
  newDate = datetime.datetime.strptime(inputDate, "%Y-%m-%d")
  return newDate.date()


def amountUpdate(msArray):
  totalAmount = 0
  for n in msArray[iN].transactionDic:
    amount = msArray[iN].transactionDic[n][0]
    totalAmount = totalAmount + amount
  msArray[iN].amount = totalAmount


iN = 0
msArray = createStockClass()
msSave=open("pickle/mainStockArray.pickle","wb")
pickle.dump(msArray,msSave)
msSave.close()
try:
  ui = open("pickle/realTData.pickle", "rb")
  realTData = pickle.load(ui)
  ui.close()
  print("Loaded real time prices")
except:
  print("Dowloading real time prices")
  realTData = getRealTimeData()

#saveData
ui = open("pickle/realTData.pickle", "wb")
pickle.dump(realTData, ui)
ui.close()



def createStockFloatV2(iN, msArray, realTData, showDividend):
  etf = msArray[iN].etf
  ticker = msArray[iN].ticker
  today = datetime.date.today()
  periodOwned = today - msArray[iN].date
  try:
    io = open("pickle/jsonData" + str(iN)+ ".pickle", "rb")
    jsonData = pickle.load(io)
    io.close()

  except:
    jsonData = oneTimeConnection(msArray[iN].ticker)
    yu = open("pickle/jsonData"+str(iN)+".pickle", "wb")
    pickle.dump(jsonData, yu)
    yu.close()
    
  price = realTData[ticker]
  if etf == False:
    price = round(float(price) / 100, 4)

  parseBuyInfoV3(msArray)
  parseDividendV2(msArray)
  updateStockTotalAmount(msArray, iN)

  mainDic = {}
  amountUpdate(msArray)
  totalAmount = int(msArray[iN].amount)
  amount = 0
  oldestDay=msArray[iN].date
  ownedFor=int((today-oldestDay).days)
  price=realTData[str(ticker)]
  amount=0
  amountBackup=0
  basePrice=0
  basePriceBackup=0
  dividend=0
  if etf==False:
    price=price/100
    
  for n in range(ownedFor):
    arrej=[]
    processedDate=oldestDay+datetime.timedelta(n)
    #update price if found in jsonData
    if str(processedDate) in jsonData['history']:
      price=round(float(jsonData['history'][str(processedDate)]['close']),3)
      if etf == False:
        price=price/100
        price=round(price,3)
      
    #update amount & basePrice if found
    if str(processedDate) in msArray[iN].transactionDic:
      amount=amount+int(msArray[iN].transactionDic[str(processedDate)][0])
      basePrice=msArray[iN].transactionDic[str(processedDate)][1]
      
      if etf == False:
        basePrice=basePrice/100
        
      todayTotal=amount*basePrice
      yesterdayTotal=amountBackup*basePriceBackup
      total=todayTotal+yesterdayTotal
      amountTotal=amount+amountBackup
      #value to be added to dic
      basePrice=round((total/amountTotal),3)
      #save values for future use
      amountBackup=amount
      basePriceBackup=basePrice
    #update dividend if found
    if str(processedDate) in msArray[iN].dividendDic:
      dividendis=(msArray[iN].dividendDic[str(processedDate)])
      dividend=dividendis+dividend
      
    
    floatisWD=round(((price-basePrice)*amount)+dividend,3)
    floatisND=round(((price-basePrice)*amount),3)
    
    
    arrej.append(price)
    arrej.append(amount)
    arrej.append(basePrice)
    arrej.append(dividend)
    arrej.append(floatisWD)
    arrej.append(floatisND)
    mainDic[str(processedDate)]=arrej
  msArray[iN].historyDic=mainDic
  return jsonData



#amount=msArray[0].amount
for n in range(len(msArray)):
  createStockFloatV2(n, msArray, realTData, True)

def theOldestDay(msArray):
  theOldestDay=datetime.date.today()
  for n in range(len(msArray)):
    date=msArray[n].date
    if date < theOldestDay:
      theOldestDay=date
  return theOldestDay
old=theOldestDay(msArray)

howLong=(datetime.date.today()-old).days

finalArray=[]
for y in range(howLong):
  datey=old+datetime.timedelta(y)
  value=0
  
  for n in range(len(msArray)):
    if str(datey) in msArray[n].historyDic:
      
      o=msArray[n].historyDic[str(datey)][4]
      value=value+o
  finalArray.append(round(value,4))

finalArrayNoDivs=[]
for y in range(howLong):
  datey=old+datetime.timedelta(y)
  value=0
  
  for n in range(len(msArray)):
    if str(datey) in msArray[n].historyDic:
      
      o=msArray[n].historyDic[str(datey)][5]
      value=value+o
  finalArrayNoDivs.append(round(value,4))


divsArray=[]
for y in range(howLong):
  datey=old+datetime.timedelta(y)
  value=0
  
  for n in range(len(msArray)):
    if str(datey) in msArray[n].historyDic:
      
      o=msArray[n].historyDic[str(datey)][3]
      value=value+o
  divsArray.append(round(value,4))
indexF=indexFundCount
plt.plot(finalArray, color="green")
plt.plot(divsArray, color="blue")
plt.axhline(0, color='blue')
plt.plot(indexFund.indexFundCount("VUKE",2000,indexFund.oldestDay), color='#a327ff')

plt.show()
timeFinish=datetime.datetime.now()
ooo=(timeFinish-timeStart).microseconds
print(ooo/1000000)


