
import requests
import sys 
import time
import offlineData
import datetime
import pickle



apiKeys=[""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",0]
#maxApi=len(apiKeys)-1
#demData={'Error Message': 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY_ADJUSTED.'}
stocksDic={'BT':'lon:bt-a'}
ApiKeyN2="lLRMkgWZYc8TYtrsm45i46pxhk8McDXuWPaYkKVmXO8bjX1t1Zqsle0Rm59f"
ApiKeyN1="8L4gZYTAF3c9PzTCVlHpZrwwTisaK77bRVTRFWfVKygr7DZdm4dakHUX5QrK"


def oneTimeConnection(nameOfStock):
  if nameOfStock == "BT":
    nameOfStock="BT.A"
  
  dctionarry={}
  res = ''
  dateNow=datetime.date.today()
  rawName=nameOfStock
  
  firstHalf='https://api.worldtradingdata.com/api/v1/history?symbol='
  lastBit=".L&sort=newest&api_token="
  #if nameOfStock in stocksDic:
    #nameOfStock=stocksDic[nameOfStock]
  #else:
    #nameOfStock=nameOfStock+str('.LON')
  link = firstHalf+nameOfStock+lastBit+ApiKeyN1
  
  try:
    res = requests.get(link).json()
  except requests.exceptions.ConnectionError:
    print('You are offline')
  print("Dowloaded "+str(nameOfStock))
  return res


#u=oneTimeConnection("VUKE")
      
    

  
	
	

	


	
	
