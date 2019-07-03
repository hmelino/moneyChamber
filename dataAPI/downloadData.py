
import requests
import sys 
import time
import offlineData
from offlineData import VUKEt
from offlineData import VMID
from offlineData import PSN


apiKeys=[""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",""apiKeyRemoved"",0]
maxApi=len(apiKeys)-1
demData={'Error Message': 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY_ADJUSTED.'}
stocksDic={'BT':'lon:bt-a'}


def oneTimeConnection(nameOfStock):
  firstHalf='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol='
  lastBit='&apikey="apiKeyRemoved"'
  if nameOfStock in stocksDic:
    nameOfStock=stocksDic[nameOfStock]
  else:
    nameOfStock=nameOfStock+str('.LON')
  link = firstHalf+nameOfStock+lastBit
  try:
    res = requests.get(link).json()
  except requests.exceptions.ConnectionError:
    print('You are offline')
  if 'Note' in res:
    print("Changing api key")
    for n in range(60,0,-1):
      print(n)
      time.sleep(1)
    res = requests.get(link).json()
  elif 'Error Message' in res:
    print('Error')
  print("Dowloaded "+str(nameOfStock))
  return res
    
    
      
    

	
	

	


	
	
