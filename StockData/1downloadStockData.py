import requests
import sys 
import time
import errorMessage
from errorMessage import *

data=['VUKE', 'VMID', 'PSN', 'HL', 'INVP', 'VOD', 'MKS', 'EVR', 'BT', 'LLOY', 'AV', 'PTEC', 'CREI', 'HMSO', 'CNCT']
stockApiLink = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=CREI.LON&outputsize=full&apikey="apiKeyRemoved""
apiKeys=[""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved""]


errorMess = errorMessage.demData
dd = stockApiLink.split("&")
cc = str(dd[1]).split("=")
symbol = cc[1]

def oneTimeConnection(nameOfStock):
	out=open(str(nameOfStock)+".py","a+")
	link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(nameOfStock)+".LON&outputsize=full&apikey="apiKeyRemoved""
	res = requests.get(link).json()
	out.write("demData="+str(res))
	out.close()
	print("Created or overwritten "+str(nameOfStock))

def dowloadWholeStockDatabase():
	i=0
	i2=0
	for n in data:
		out=open(str(data[i])+".py","a+")
		if n = "BT":
			link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(data[i])+"&outputsize=full&apikey="+str(apiKeys[i2])"
			res = requests.get(link).json()
		else:
			adjustedLink="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+str(data[i])+".LON&outputsize=full&apikey="+str(apiKeys[i2])
			res = requests.get(adjustedLink).json()
		if res == errorMess:
			i2=i2+1
			res = requests.get(adjustedLink).json()
		else:pass
		out.write("demData="+str(res))
		out.close()
		i=i+1
	


	
start = time.time()
#dowloadWholeStockDatabase()
oneTimeConnection("")
end= time.time()
print(end-start)
