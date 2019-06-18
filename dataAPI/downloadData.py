
import requests
import sys 
import time
apiKeys=[""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved""]

def oneTimeConnection(nameOfStock):
	i2=0
	link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(nameOfStock)+".LON&outputsize=compact&apikey="+apiKeys[i2]
	res = requests.get(link).json()
	if res == "Note': 'Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency.":
			print("contains error")
			i2=i2+1
			res = requests.get(link).json()
			
	else:pass
	print("Dowloaded "+str(nameOfStock))
	print("used"+apiKeys[i2])
	
	return res
	
	

	


	
	
