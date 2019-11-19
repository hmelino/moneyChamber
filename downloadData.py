import requests
import sensData 
from sensData import apiKey
apiKeyV2="lLRMkgWZYc8TYtrsm45i46pxhk8McDXuWPaYkKVmXO8bjX1t1Zqsle0Rm59f"

def oneTimeConnection(stockName):
	if stockName == "BT":
		stockName+=".A"
	fHalf='https://api.worldtradingdata.com/api/v1/history?symbol='
	sHalf=".L&sort=newest&api_token="
	try:
		res = requests.get(fHalf+stockName+sHalf+apiKeyV2).json()
		print("Dowloaded "+str(stockName))
		return res
	except requests.exceptions.ConnectionError:
		print('You are offline')

