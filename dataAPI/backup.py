
import buyInfo
from buyInfo import *
import dividendInfo
from dividendInfo import *
import sys
import re
#just for developing
import pickle
import datetime


def parseBuyInfo(mainStockArray):
  arrej=[]
  m=open('buyInfo.py','r')
  i=m.readlines()
  for n in range(len(i)):
    p=i[n]
    r=re.sub('[a-zA-Z{=""}]','',p)
    s=re.split(',',r)
    buyInfoDict={}
    for n in range(len(s)):
      o=re.split(':',s[n])
      buyInfoDict[o[0]]=int(o[1])
    arrej.append(buyInfoDict)
  return arrej
  
def parseDividendInfo():
  arrej=[]
  m=open('dividendInfo.py','r')
  i=m.readlines()
  for n in range(len(i)):
    p=i[n]
    #VOD={'2018-11-28':1.27}
    
    r=re.sub('[{="":\n},]','',p)
    s=re.split("'",r)
    #['VOD', '2018-11-28', '1.27']
    
    print('s='+str(s))
    print(len(s))
    howManyDivs=(((len(s))-1)/2)+1
    print('how many divs ='+str(howManyDivs))
    
    processedDate=datetime.datetime.strptime(s[1],'%Y-%m-%d').date()
    
    #s=['EVR', '2018-11-21', '0.75', '2019-03-06', '4.34']
    
    for z in range(1,int(howManyDivs),1):
      print('round'+str(z)+'--------')
      divTotal=0
      divName=s[0]
      print('divName='+str(divName))
      divValue=s[2*z]
      print('divValue='+str(divValue))
      for t in range(len(mainStockArray)):
        #t is ticker number 
        if divName in mainStockArray[t].ticker:
          for n in sorted(mainStockArray[t].historyDic):
            print(n)
            dividendInArray=mainStockArray[t].historyDic[n][3]
            newDic={}
            
            if n == processedDate:
              divTotal=divTotal+float(divValue)
              dividendInArray=dividendInArray+divTotal
              print(dividendInArray)
              #mainStockArray[t].historyDic[n][3]=divTotal
              print('divTotal='+str(divTotal))
            else:
              dividendInArray=dividendInArray+divTotal
              #mainStockArray[t].historyDic[n][3]=divTotal
              print('divTotal='+str(divTotal))
              print(dividendInArray)
  return mainStockArray
  
  
  
pickle_out=open('pickle/MainStockArray.pickle','rb')
mainStockArray=pickle.load(pickle_out)

m=parseDividendInfo()
  
  
  


  
  
  




