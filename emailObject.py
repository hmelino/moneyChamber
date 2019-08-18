import datetime
from datetime import date
import emailData
from emailData import *

		
class Stock:
  def __init__(self,ticker,amount,date,transactionDic,price,etf,historyDic,dividendDic,timeStamp,positionOrders):
    self.ticker = ticker
    self.amount = amount
    self.date = date
    self.transactionDic=transactionDic
    self.price=price
    self.etf=etf
    self.historyDic=historyDic
    self.dividendDic=dividendDic
    self.timeStamp=timeStamp
    self.positionOrders=positionOrders


	
def createStockClass():
  bigArray=[]
  etfArray=["VMID","VUKE"]
  
  print("creating MainStockArray")
  data = emailData.demData
  i = 0
  for n in range(int(len(data)/12)):
    etf=False
    #check if etf
    if data[4+i] in etfArray:
      etf=True
    #data format
    dateM=data[1+i].split(" ")[0]
    demm=datetime.datetime.strptime(str(dateM),"%Y.%m.%d").date()
    myObj=Stock(data[4+i],data[3+i],demm,0,data[5+i],etf,{},{},0,{}) 
    bigArray.append(myObj)
    i=i+12
  return bigArray
  
  

  

  
  





