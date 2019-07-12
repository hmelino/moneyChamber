import downloadData
from downloadData import *
import functionsLibrary
from functionsLibrary import *


def createData(selectedStock,mainStockArray):
  print(" ")

  transactionDic=mainStockArray[selectedStock].transactionDic
  stockTicker=mainStockArray[selectedStock].ticker
  
  
  
  firstDay=mainStockArray[selectedStock].date
  
  
  #dowload all stock data avaiable
  jsonData=downloadData.oneTimeConnection(stockTicker)
  #print(jsonData)

  # define date now
  dateNow=datetime.datetime.today().date()
  
  howManyDays=(dateNow-firstDay)
  
  ownershipPeriod=howManyDays.days
  
  # create countable unit of 1 day
  oneDay=datetime.timedelta(1)
  
  print("- "+str(stockTicker)+"was bought "+str(ownershipPeriod)+" days ago")
  
  
  
  
  #count total Amount owning by today 
  totalAmountToday=0
  for n in transactionDic.values():
    totalAmountToday=totalAmountToday+int(n)
  amount=totalAmountToday
  
  stockTotalTotal=totalAmountToday*mainStockArray[selectedStock].price
  
  priceDic=functionsLibrary.createPriceDic(ownershipPeriod,dateNow,jsonData,transactionDic)
  #print(priceDic)
  
  
  # create time stamp data from JSONdata
  timeStampRaw=jsonData['Meta Data']['3. Last Refreshed']
  timeStamp=datetime.datetime.strptime(timeStampRaw,'%Y-%m-%d').date()
  mainStockArray[selectedStock].timeStamp=timeStamp
  print('- added time stamp')
  #end
  
  
  priceDic=functionsLibrary.fixZeroPriceDay(priceDic,oneDay)
  priceDic=functionsLibrary.fixPriceAnomalies(mainStockArray,priceDic,selectedStock)
  
  historyDic=functionsLibrary.createHistoryDic(totalAmountToday,mainStockArray,selectedStock,priceDic)
  
  
  # update previous base prices in History Dictionary
  historyDic=functionsLibrary.createPreviousBasePrice(historyDic,selectedStock,mainStockArray)
  
  
  
  #create Array for all days (firstBuy-today)
  dateArray=functionsLibrary.dateArray(mainStockArray)
  
  

  # create floatArray from historyDic
  floatArray=functionsLibrary.floatArrayFromDic(historyDic,dateArray)
  
  #save data
  mainStockArray[selectedStock].historyDic=historyDic
  offline=open('offlineData/leStorage.py','a+')
  offline.write(str(selectedStock)+'='+str(historyDic))
  offline.close()
  

  
