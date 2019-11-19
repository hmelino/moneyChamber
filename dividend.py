import pickle
import datetime
import matplotlib.pyplot as plt
today=datetime.datetime.today()

q=open("pickle/mainStockArray.pickle","rb")
msArray=pickle.load(q)
q.close()

class Dividend:
	def __init__(self,ticker,value):
		self.ticker=ticker
		self.value=value
		
class PotentialBuy:
	def __init__(self,price,amount):
		self.price=price
		self.amount=amount


def createDivDictionarie():
	divDict={}
	for stock in msArray:
		for date in msArray[stock].dividendInfo:
			if date != "0":
				divPayment=msArray[stock].dividendInfo[date]
				divAmount=msArray[stock].historyDic[date].amount
				value=round(divPayment/divAmount,3)
				#print(f"{stock}|{divPayment}|{value}")
				if date[5:] not in divDict:
					divDict[date[5:]]=[]
				divDict[date[5:]].append(Dividend(stock,value))
				
	return divDict
	
dict=createDivDictionarie()

today=datetime.datetime.today().date()


yearList=[]
for d in range(365):
	todaysDividend=0
	day=str(today+datetime.timedelta(d))[5:]
	if str(day) in dict:
		for stock in range(len(dict[day])):
			divValue=dict[day][stock].value
			todaysDividend=divValue
			stockName=dict[day][stock].ticker
			amount=msArray[stockName].amount
			yearList.append(todaysDividend*amount)
			print(f"|{round(todaysDividend*amount,2)}| {stockName}|{day}|{todaysDividend}|{amount}")
	else:
		yearList.append(todaysDividend)
		
plt.plot(yearList)
plt.show()
		

	
