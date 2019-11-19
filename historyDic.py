import downloadData
from downloadData import oneTimeConnection
import pickle
import datetime


class RealTDataClass:
 def __init__(self,date,data):
  self.date=date
  self.data=data

class HistoryPrice:
	def __init__(self,basePrice,amount,profit,dividends):
		self.basePrice=basePrice
		self.amount=amount
		self.profit=profit
		self.dividends=dividends

def stockFloat(stock,msArray):
	today=datetime.datetime.today()
	try:
		loaded=pickle.load(open("pickle/"+str(stock)+".pickle","rb"))
		jsonData=loaded.data
		dataDate=(today.date()-loaded.date.date()).days
		if dataDate <= 2:
			print(f"Loaded {stock}")
		else:
			print(f"Dowloaded stock data is old {dataDate} days")
			causeError()
	except:
		jsonData=oneTimeConnection(stock)
		pickle.dump(RealTDataClass(datetime.datetime.today(),jsonData),open("pickle/"+str(stock)+".pickle","wb"))
		
		
	periodOwned=(datetime.datetime.today()-msArray[stock].firstBuy).days
	
	#create history dictionary w previous base price
	historyDic={}
	amountNow, priceNow=msArray[stock].buyInfo[str(msArray[stock].firstBuy.date())]
	if msArray[stock].etf == False:
		priceNow/=100
	priceBefore=priceNow
	amountBefore=amountNow
	#firstDay
	historyDic[str(msArray[stock].firstBuy.date())]=HistoryPrice(priceNow,amountNow,0,0)
	profit=0
	dividend=0
	
	
	for dayN in range(1,periodOwned):
		day=str((msArray[stock].firstBuy+datetime.timedelta(dayN)).date())
		#if there was transaction that day
		if day in msArray[stock].buyInfo:
			amountNow,priceNow=msArray[stock].buyInfo[day]
			if msArray[stock].etf==False:
				priceNow/=100
			totalNow=amountNow*priceNow
			totalBefore=amountBefore*priceBefore
			amountNow+=amountBefore
			priceNow=(totalNow+totalBefore)/amountNow
			amountBefore,priceBefore=amountNow,priceNow
		#if markets were open that day
		if day in jsonData['history']:
			realPrice=float(jsonData['history'][day]['close'])
			if msArray[stock].etf==False:
				realPrice/=100
			profit=((realPrice-priceNow)*amountNow)+dividend
		#if recieved dividend that day
		if day in msArray[stock].dividendInfo:
			dividend+=msArray[stock].dividendInfo[day]
		historyDic[day]=HistoryPrice(round(priceNow,3),amountNow,profit,dividend)
	msArray[stock].historyDic=historyDic
