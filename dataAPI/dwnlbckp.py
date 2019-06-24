
import requests
import sys 
import time
apiKeys=[""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved""]
demData={'Error Message': 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY_ADJUSTED.'}

def oneTimeConnection(nameOfStock):
	i2=0
	link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(nameOfStock)+".LON&outputsize=full&apikey="+apiKeys[i2]
	res = requests.get(link).json()
	if res == demData:
		print("contains error")
		i2=i2+1
		res = requests.get(link).json()
	elif ["Error Message"]in res:
		print("Ticker error")
		res = requests.get(link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(nameOfStock)+"&outputsize=full&apikey="+apiKeys[i2])
	else:pass
	print("Dowloaded "+str(nameOfStock))
	print("used"+apiKeys[i2])
	
	return res

	
	

	


	
	
