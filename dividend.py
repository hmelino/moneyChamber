import pickle
import datetime
import matplotlib.pyplot as plt
today=datetime.datetime.today()
def loadMsArray():
	q=open("pickle/mainStockArray.pickle","rb")
	msArray=pickle.load(q)
	q.close()
	return msArray

class Dividend:
	def __init__(self,ticker,value):
		self.ticker=ticker
		self.value=value
		
class PotentialBuy:
	def __init__(self,price,amount):
		self.price=price
		self.amount=amount
		
def countYeld():
	for stock in msArray:
		stockValue=msArray[stock].price
		if msArray[stock].etf==True:
			stockValue*=100
		stockValue/=100
		payouts=[]
		for date in msArray[stock].dividendInfo:
			if date != "0":
				day=datetime.datetime.strptime(date,"%Y-%m-%d")
				if (today-day.date()).days <= 365:
					amount=msArray[stock].historyDic[date].amount
					div=msArray[stock].dividendInfo[date]
					payouts.append(div/amount)
		yeld=round(((sum(payouts))/stockValue)*100,2)
		print(f"Yeld of {stock} is {yeld}%")

def createDivDictionarie():
	divDict={}
	for stock in msArray:
		for date in msArray[stock].dividendInfo:
			if date != "0":
				divPayment=msArray[stock].dividendInfo[date]
				divAmount=msArray[stock].historyDic[date].amount
				value=round(divPayment/divAmount,3)
				if date[5:] not in divDict:
					divDict[date[5:]]=[]
				divDict[date[5:]].append(Dividend(stock,value))
	return divDict

def processAllDividends():
	yearsTotalList=[]
	yearsTotal=0
	yearList=[]
	for d in range(366):
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
				yearsTotal+=todaysDividend*amount
		else:
			yearList.append(todaysDividend)
		yearsTotalList.append(yearsTotal)
	return yearList,yearsTotalList,yearsTotal


msArray=loadMsArray()
dict=createDivDictionarie()
today=datetime.datetime.today().date()
yearList,yearsTotalList,yearsTotal=processAllDividends()
plt.plot(yearList)
plt.plot(yearsTotalList)
plt.show()
print(f"Total div payout is {yearsTotal}")
qq=countYeld()
