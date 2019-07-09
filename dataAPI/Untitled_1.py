class Stock:
		def __init__(self,ticker,amount,date,transactionDic,price,etf,historyDic,dividendDic):
			self.ticker = ticker
			self.amount = amount
			self.date = date
			self.transactionDic=transactionDic
			self.price=price
			self.etf=etf
			self.historyDic=historyDic
			self.dividendDic=dividendDic
