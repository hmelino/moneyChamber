import requests
import sensData 
import pickle
from sensData import apiKey

def oneTimeConnection(stockName):
	if stockName == "BT":
		stockName+=".A"
	fHalf='https://api.worldtradingdata.com/api/v1/history?symbol='
	sHalf=".L&sort=newest&api_token="
	try:
		res = requests.get(fHalf+stockName+sHalf+apiKey).json()
		print("Dowloaded "+str(stockName))
		return res
	except requests.exceptions.ConnectionError:
		print('You are offline')

