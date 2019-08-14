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

		



	
def createStockClass():
  print("creating MainStockArray")
  data = emailData.demData
  i = 0
  for n in range(int(len(data)/12)):
    #data format
    dateM=data[1+i].split(" ")[0]
    demm=datetime.datetime.strptime(str(dateM),"%Y.%m.%d").date()
    myObj=Stock(data[4+i],data[3+i],demm,0,data[5+i],False,{},{},0,{}) 
    bigArray.append(myObj)
    i=i+12
  return bigArray
  
  

  

  
  
#l=createStockClass()
#u=createStockJsonClass()

  

#p=convert_to_dict(l)
#print(p['ticker'])













