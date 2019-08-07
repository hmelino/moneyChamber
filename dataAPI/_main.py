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
import buyInfo 
from buyInfo import *
import sys 
import offlineData
from offlineData import *
import createStockData
from createStockData import *
import numpy as np
import notification



start = time.time()
	
############################################################################################################################################         start of program


#check is MainStockArray is saved
mainStockArray=functionsLibrary.isMainStockArraySaved()

#Process mainStockArray
buyInfo=buyInfoParse.parseBuyInfo(mainStockArray)
dictionary={}
for n in range(len(buyInfo)):
  mainStockArray[n].transactionDic=buyInfo[n]
  
  
#check date of saved Data
if functionsLibrary.checkDateOfSavedData(mainStockArray) == True:pass

else:
  for n in range(15):
    o=createStockData.createData(n,mainStockArray)
  
 

mainStockArray=functionsLibrary.multipyETFprice(mainStockArray)
dateArray=functionsLibrary.dateArray(mainStockArray)
mainStockArray=buyInfoParse.parseDividendInfo(mainStockArray)
floatArray=[]

#create dateArray
dejtArray=[]
for n in range(len(mainStockArray)):
  dejt=str(mainStockArray[n].date)
  dejtArray.append(dejt)



#create Float Array
uArray=functionsLibrary.createFloatArrayV2(mainStockArray,dateArray,True)


kolokolo=[]
for n in range(len(mainStockArray)):
  l=(mainStockArray[n].ticker)
  kolokolo.append(l)
print(kolokolo)
  
functionsLibrary.saveMainStockArray(mainStockArray)

gray=np.array(uArray)
black=gray.sum(axis=0)
#fix if last number is 0
#for n in black:
  #if black[n] == 0:
    #print("found mistake")
    #black=black[:n]


end = time.time()
print(end-start)
def countAccTotalValue():
  accTotalValue=0
  for n in range(len(mainStockArray)):
    amount=float(mainStockArray[n].amount)
    price=float(mainStockArray[n].price)
    for m in mainStockArray[n].historyDic:
      div=mainStockArray[n].historyDic[m][3]
      value=((amount*price)/100)+div
      break
    accTotalValue=accTotalValue+value
  return round(accTotalValue,2)
def countTotalDivs():
  value=0
  for n in range(len(mainStockArray)):
    amount=float(mainStockArray[n].amount)
    price=float(mainStockArray[n].price)
    for m in mainStockArray[n].historyDic:
      div=mainStockArray[n].historyDic[m][3]
      value=value+div
      break
  return round(float(value),2)
print(countTotalDivs())
    
    
accValue=countAccTotalValue()
totalProfit=black[len(black)-1]
print(totalProfit)

#percent increase 
percent= ((totalProfit/countAccTotalValue())*100)
percent=round(percent,2)
print(percent)

notification.schedule("Today your portfolio is up by £"+str(round(black[len(black)-1]))+"\n "+str(percent)+"%")


plt.plot(black)
plt.axhline(0, color='blue')
plt.axhline(black[len(black)-1], color='lightseagreen')
plt.axhline(countTotalDivs(),color='lightseagreen')
plt.show()

		





