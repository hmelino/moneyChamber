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
def reinvest(ticker):
	pass
	


dividendCalendarV3={}
for stockN in range(len(msArray)):
	for date in msArray[stockN].dividendDic:
		if date != "0":
			innerArray=[]
			name=(msArray[stockN].ticker)
			#dateV2=datetime.datetime.strptime(date,"%Y-%m-%d")
			value=msArray[stockN].dividendDic[date]
			if date == str(today.date()):
				amount=msArray[stockN].amount
			else:
				amount=msArray[stockN].historyDic[date][1]
			dividend=round(value/amount,3)
			#innerArray.append(date[5:])
			innerArray.append(name)
			innerArray.append(dividend)
		if str(date[5:]) in dividendCalendarV3:
				print("Already exist")
				m=dividendCalendarV3[str(date[5:])]
				m+=innerArray
				dividendCalendarV3[str(date[5:])]=m
		else:
			dividendCalendarV3[str(date[5:])]=innerArray

stockAmountDic={stock.ticker:stock.amount for stock in msArray}


totalDivValueArray=[]
dividend_array=[]
totalDiv=0

today=datetime.datetime.today()

for n in range(365):
 dividend_value=0
 
 day=today+datetime.timedelta(n)
 processedDay=str(day.month)+"-"+str(day.day)
 stringDay=day.strftime("%m-%d")
 
 if stringDay in dividendCalendarV3:
  name=(dividendCalendarV3[stringDay][0])
  print(name)
  print(stringDay)
  amount_now=stockAmountDic[name]
  print(amount_now)
  dividend_value=amount_now*dividendCalendarV3[stringDay][1]
  totalDiv+=dividend_value
 dividend_array.append(dividend_value)
 totalDivValueArray.append(totalDiv)
 

plt.plot(dividend_array)
plt.plot(totalDivValueArray)
plt.grid()
plt.show()





