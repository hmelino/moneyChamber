import datetime
import sys
import pickle
from etfCheck import etfCheck

class StockV2():
	def __init__(self,amount,firstBuy,price):
		self.amount = amount
		self.firstBuy = firstBuy
		self.price = price
		
def loadEmailData():
	try:
		from emailStatement import statement
		return statement
	except:
		print("Missing Email Statement")
		#function here to manually create email report
		sys.exit()
		
def processMonthlyStatement():
	data=loadEmailData()
	return {data[4+(12*f)]:StockV2(int(data[3+(12*f)]),  datetime.datetime.strptime(data[1+(12*f)],"%Y.%m.%d %H:%M"),float(data[5+(12*f)])) for f in range(int(len(emailData.demData)/12))}
	
def loadMsArray():
	return pickle.load(open("pickle/msArray.pickle","rb"))
	
def saveMsArray(data):
	pickle.dump(data,open("pickle/msArray.pickle","wb"))
	
def getMsArray():
	try:
		return loadMsArray()
	except:
		data=processMonthlyStatement()
		etfCheck(data)
		saveMsArray(data)
		return data
		
