import datetime
import emailData
from emailData import *
data=emailData.demData
		

class StockV2():
	def __init__(self,amount,firstBuy,price):
		self.amount = amount
		self.firstBuy = firstBuy
		self.price = price
		

def processMonthlyStatement():
	data=emailData.demData
	return {data[4+(12*f)]:StockV2(int(data[3+(12*f)]),  datetime.datetime.strptime(data[1+(12*f)],"%Y.%m.%d %H:%M"),float(data[5+(12*f)])) for f in range(int(len(emailData.demData)/12))}
