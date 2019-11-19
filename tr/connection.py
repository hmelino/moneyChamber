import requests
import sys 
stockApiLink = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=VUKE.LON&outputsize=full&apikey="apiKeyRemoved""




#newlink="https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=VUK&apikey="apiKeyRemoved""
def openWebsite():
	out=open("webDataResult3.py","a+")
	res = requests.get(stockApiLink).json()
	#print(res['Time Series (Daily)']['2019-06-07']['4. close'])
	out.write("demData="+str(res))
	#out.write(str(res))
	out.close()
	

openWebsite()
	

