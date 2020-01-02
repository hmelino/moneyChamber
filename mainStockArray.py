def updateStockAmountTotal(msArray):
	import datetime
	for stock in msArray:
		msArray[stock].amount=msArray[stock].historyDic[datetime.datetime.today().strftime("%Y-%m-%d")].amount