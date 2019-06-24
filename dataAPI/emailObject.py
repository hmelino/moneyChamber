import datetime
from datetime import date
import emailData
from emailData import *
etfArray=["VMID","VUKE"]
myArray=[]

		

def etfCheck():
	for n in range(len(myArray)):
		for i in range(len(etfArray)):
			if etfArray[i]==myArray[n].ticker:
				myArray[n].etf=True
			else:
				pass

	
def createStockClass():
	#create Class
	class Stock (object):
		def __init__(self,ticker,amount,date,arrej,price,etf):
			self.ticker = ticker
			self.amount = amount
			self.date = date
			self.arrej=arrej
			self.price=price
			self.etf=etf

	data = emailData.demData
	i = 0
	for n in range(int(len(data)/12)):
		
		#data format
		dateM=data[1+i].split(" ")[0]
		demm=datetime.datetime.strptime(str(dateM),"%Y.%m.%d").date()
		myArray.append(Stock(data[4+i],data[3+i],demm,0,data[5+i],False))
		#print(data[4+i],data[3+i],demm,0,data[5+i],False)
		
		i=i+12
		
	etfCheck()
	return myArray
	








