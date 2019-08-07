import datetime
from datetime import date
import emailData
from emailData import *
import pickle
import StockClass
from StockClass import Stock



myArray=[]
bigArray=[]
etfArray=["VMID","VUKE"]

		

def etfCheck(myArray):
	for n in range(len(myArray)):
		for i in range(len(etfArray)):
			if etfArray[i]==myArray[n].ticker:
				myArray[n].etf=True
			else:
				pass

	
def createStockClass():
  print("creating MainStockArray")
  data = emailData.demData
  i = 0
  for n in range(int(len(data)/12)):
    #data format
    dateM=data[1+i].split(" ")[0]
    demm=datetime.datetime.strptime(str(dateM),"%Y.%m.%d").date()
    myObj=Stock(data[4+i],data[3+i],demm,0,data[5+i],False,{},{},0)
    bigArray.append(myObj)
    i=i+12
  return bigArray
  
  
def convert_to_dict(obj):
  
  
  #  Populate the dictionary with object meta data 
  obj_dict = {
    "__class__": obj.__class__.__name__,
    "__module__": obj.__module__
  }
  
  #  Populate the dictionary with object properties
  obj_dict.update(obj.__dict__)
  
  return obj_dict
  
def createStockJsonClass():
  print("creating MainStockArray")
  data = emailData.demData
  i = 0
  for n in range(int(len(data)/12)):
    #data format
    dateM=data[1+i].split(" ")[0]
    demm=datetime.datetime.strptime(str(dateM),"%Y.%m.%d").date()
    myObj=Stock(data[4+i],data[3+i],demm,0,data[5+i],False,{},{},0)
    i=i+12
    stocko=convert_to_dict(myObj)
    bigArray.append(stocko)
    
    
  #etfCheck(bigArray)
  return bigArray
  
  
#l=createStockClass()
#u=createStockJsonClass()

  

#p=convert_to_dict(l)
#print(p['ticker'])













