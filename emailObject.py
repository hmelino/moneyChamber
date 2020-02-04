import sys
import datetime
import pickle
from etfCheck import etfCheck
from emailStatement import statement

class StockV2:
	oldestDay=datetime.date.today()

	def __init__(self,amount,firstBuy,price):
		self.amount = amount
		self.firstBuy = firstBuy
		self.price = price

		if StockV2.oldestDay > self.firstBuy.date():
			StockV2.oldestDay=self.firstBuy.date()

	def howManyDays(self,cls):
		return (datetime.date.today() - StockV2.oldestDay).days



def getMsArray():
	try:
		return loadMsArray()
	except:
		data=processMonthlyStatement()
		etfCheck(data)
		saveMsArray(data)
		return data

def saveMsArray(data):
	pickle.dump(data,open("pickle/msArray.pickle","wb"))

def processMonthlyStatement():
	data=loadEmailData()
	return {data[4+(12*f)]:StockV2(int(data[3+(12*f)]),  datetime.datetime.strptime(data[1+(12*f)],"%Y.%m.%d %H:%M"),float(data[5+(12*f)])) for f in range(int(len(statement)/12))}

def loadEmailData():
	try:
		from emailStatement import statement
		return statement
	except:
		print("Missing Email Statement")
		#function here to manually create email report
		sys.exit()

