import requests
import datetime
namesArray=['VUKE', 'VMID', 'PSN', 'HL', 'INVP', 'VOD', 'MKS', 'EVR', 'BT', 'LLOY', 'AV', 'PTEC', 'CREI', 'HMSO', 'CNCT']



start=datetime.datetime.today()
res=requests.get('"secretWebsiteForRealTimeData"').json()
indexNum=0
for p in range(len(namesArray)):
  for n in res:
    if n['name']==namesArray[p] and n['margin']==1:
      print(n['prettyName'])
      print(n['realPrice']['buy'])
    #print(n)
    #for l in n:
      #print(n[l])
      print(" ")
    
    #print(n['prettyName'])
    #print(n['price']['buy'])


