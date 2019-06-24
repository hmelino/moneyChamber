
import requests
import sys 
import time
apiKeys=[""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",0]
maxApi=len(apiKeys)-1
demData={'Error Message': 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY_ADJUSTED.'}
stocksDic={'BT':'LON:BT-A','VUKE':'VUKE.LON','LLOY':'LON:LLOY'}

def oneTimeConnection(nameOfStock):
	i2=0
	link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(nameOfStock)+".LON&outputsize=full&apikey="+apiKeys[i2]
	
	res = requests.get(link).json()
	print(nameOfStock)
	if nameOfStock in stocksDic:
		print('found match in dictionary')
		print(stocksDic[nameOfStock])
		
	#if nameOfStock=="BT":
			#link2 = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=LON:BT-A&outputsize=full&apikey="+apiKeys[i2]
			#res = requests.get(link2).json()
			#if 'Note' in res:
				#i2=i2+1
				#if i2==maxApi:
					#i2=0
					#res = requests.get(link2).json()
				#else:
					#res = requests.get(link2).json()
			#else: pass
			
		
	elif 'Note' in res:
			print("changing api key")
			i2=i2+1
			if i2==maxApi:
				print("restarting API")
				i2=0
			else:pass
			for n in range(60,0,-1):
					print(n)
					time.sleep(1)
			
			res = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(nameOfStock)+".LON&outputsize=full&apikey="+apiKeys[i2]).json()
			
	else:pass
	print("Dowloaded "+str(nameOfStock))
	print("used"+apiKeys[i2])
	return res

	
	

	


	
	
