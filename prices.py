import time
import os
import pickle
import requests
import sys

def addPrices(self,stockName,apiKey):
		class Day:
			def __init__(self,basePrice,amount,stockPrice,etf,dividend,deposits):
				if etf == False:
					stockPrice/=100
					basePrice/=100
				self.profit=round(((stockPrice-basePrice)*amount)+dividend,3)
				self.amount=amount
				self.stockPrice=stockPrice
				self.basePrice=basePrice
				self.dividendPaid=dividend
				self.totalDeposits=deposits
		
		def oneTimeConnection(stockName=stockName):

			todayUnixTime=time.time()
			def downloadFreshStockData():
				try:
					data=requests.get(f'https://api.worldtradingdata.com/api/v1/history?symbol={stockName}.L&sort=newest&api_token={apiKey}').json()['history']
					return data
				except IndexError:
					print('Connection error')
					sys.exit()

			path=os.path.join(os.path.dirname(__file__),f"pickle\\{stockName}.pickle")
			if stockName == "BT":
				stockName+=".A"
			try:
				res=pickle.load(open(path,'rb'))
				if todayUnixTime - os.path.getmtime(path) > 86400:
					res=downloadFreshStockData()
					print(f"Old data for {stockName}, dowloaded new one")
					pickle.dump(res,open(path,'wb'))
			except (FileNotFoundError):
				res = downloadFreshStockData()
				print("Downloaded "+str(stockName))
				pickle.dump(res,open(path,'wb'))
			return res
			
		def newBasePrice():
			if day != firstDay:
				bfAmount=amount
				newAmount,newPrice=self.ordersData[stockName][stringDay]
				bfPrice=basePrice
				totalBefore=bfAmount*bfPrice
				totalNew=newAmount*newPrice
				totalAmount=bfAmount+newAmount
				newBasePrice=(totalBefore+totalNew)/totalAmount
				return round(newBasePrice,3),totalAmount
			return basePrice,amount
		
		totalStockDividends=0
		priceData=oneTimeConnection()
		stockPrice=0
		firstDay=self.db[stockName].date
		strFirstDay=self.strDay(firstDay)
		amount=float(self.ordersData[stockName][strFirstDay][0])
		basePrice=float(self.ordersData[stockName][strFirstDay][1])
		etf=self.db[stockName].etf
		for day in self.db[stockName].history.keys():
			stringDay=self.strDay(day)

			# add dividends 
			if stockName in self.dividendData:
				if stringDay in self.dividendData[stockName]:
					totalStockDividends+=self.dividendData[stockName][stringDay]
					self.db[stockName].dividendTotal+=totalStockDividends
			#count new base price
			if stringDay in self.ordersData[stockName]:
				basePrice,amount=newBasePrice()
			#update stock price if markets were opened
			if stringDay in priceData:
				stockPrice=float(priceData[stringDay]['close'])
			self.db[stockName].history[day]=Day(basePrice,amount,stockPrice,etf,totalStockDividends,0)