from oldestDay import whatsOldestDay
import datetime

def historyProfit(msArray,stockFloat):
	floatArray=[]
	for stockName in msArray:
		q=stockFloat(stockName,msArray)
		floatArray.append({f:msArray[stockName].historyDic[f].profit for f in msArray[stockName].historyDic})
	

	oldestDay=whatsOldestDay(floatArray)

	totalFloat=[]
	today=datetime.datetime.today().date()
	portfolioOwned=(today-oldestDay.date()).days
	for day in range(portfolioOwned):
		processedDay=str((oldestDay + datetime.timedelta(day)).date())
		dayTotal=0
		for stock in msArray:
			if processedDay in msArray[stock].historyDic:
				dayTotal+=msArray[stock].historyDic[processedDay].profit
		totalFloat.append(dayTotal)
	return totalFloat
