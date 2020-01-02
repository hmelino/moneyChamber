import requests
import datetime
from sensData import realTwebsite
namesArray=['VUKE', 'VMID', 'PSN', 'HL', 'INVP', 'VOD', 'MKS', 'EVR', 'BT', 'LLOY', 'AV', 'PTEC', 'CREI', 'HMSO', 'CNCT']



def getRealTimeData():
  dArray=[]
  todaysRealTime={}
  start=datetime.datetime.today()
  res=requests.get(realTwebsite).json()
  indexNum=0
  for p in range(len(namesArray)):
    for n in res:
      if n['name']==namesArray[p] and n['margin']==1:
        if 'realPrice' in n:
          price=float(n['realPrice']['buy'])
          name=n['name']
          
          if str(name) in ["VUKE","VMID"]:
          	
           todaysRealTime[name]=price
          else:
           todaysRealTime[name]=price/100
  return todaysRealTime
        



