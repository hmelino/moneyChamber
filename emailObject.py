import datetime
import emailData
from emailData import *
data=emailData.demData
		
"""class Stock:
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
"""

class StockV2():
	def __init__(self,amount,firstBuy,price):
		self.amount = amount
		self.firstBuy = firstBuy
		self.price = price
		
	


def stockList():
	data=emailData.demData
	return {data[4+(12*f)]:StockV2(int(data[3+(12*f)]),  datetime.datetime.strptime(data[1+(12*f)],"%Y.%m.%d %H:%M"),float(data[5+(12*f)])) for f in range(int(len(emailData.demData)/12))}
	

	
"""
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
  """
  
  

  

  
  





