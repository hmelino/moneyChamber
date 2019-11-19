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
	


dividendCalendarV3={}
for stockN in range(len(msArray)):
	for date in msArray[stockN].dividendDic:
		if date != "0":
			innerArray=[]
			name=(msArray[stockN].ticker)
			value=msArray[stockN].dividendDic[date]
			if date == str(today.date()):
				amount=msArray[stockN].amount
			else:
				amount=msArray[stockN].historyDic[date][1]
			dividend=round(value/amount,3)
			innerArray.append(name)
			innerArray.append(dividend)
		if str(date[5:]) in dividendCalendarV3:
				m=dividendCalendarV3[str(date[5:])]
				m+=innerArray
				dividendCalendarV3[str(date[5:])]=m
		else:
			dividendCalendarV3[str(date[5:])]=innerArray

stockAmountDic={stock.ticker:stock.amount for stock in msArray}

def processData(compound:bool(),ticker:str(),deposits:bool()):
	stockPrice=None
	if compound is True:
		for f in range(len(msArray)):
			if msArray[f].ticker == ticker:
				stockPrice=float(msArray[f].price)
				print(f"found price for {ticker} ")
	totalDivValueArray=[]
	dividendArray=[]
	totalDiv=0
	freeMoney=0
	for n in range(366):
		if n%30 is 0:
			freeMoney+=100
		dividend_value=0
		day=datetime.datetime.today()+datetime.timedelta(n)
		stringDay=day.strftime("%m-%d")
		
		if stringDay in dividendCalendarV3:
			for q in range(int(len(dividendCalendarV3[stringDay])/2)):
			name=(dividendCalendarV3[stringDay][0])
			#0,1,2,3
			
			
			if compound is True:
				moreShares=int(freeMoney/stockPrice)
				if moreShares>0:
					print(f"bought {moreShares} share")
					print(n)
					stockAmountDic[ticker]+=moreShares
					freeMoney-=moreShares*stockPrice
					moreShares=0
			amount_now=stockAmountDic[name]
			dividend_value=amount_now*dividendCalendarV3[stringDay][1]
			totalDiv+=dividend_value
			freeMoney+=dividend_value
			
		dividendArray.append(dividend_value)
		totalDivValueArray.append(totalDiv)
	return dividendArray,totalDivValueArray

dividendArray,totalDivValueArray=processData(True,"VUKE",True)

plt.plot(dividendArray)
plt.plot(totalDivValueArray)





plt.grid()
plt.show()

print(f"total value is {totalDivValueArray[-1]}")





