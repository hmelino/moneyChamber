
import buyInfo
from buyInfo import *
import dividendInfo
from dividendInfo import *
import sys
import re
#just for developing
import pickle
import datetime
import ast


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
  
def parseBuyInfoV2(mainStockArray):
  arrej=[]
  arr=[]
  m=open('buyInfo.py','r')
  i=m.readlines()
  for n in range(len(i)):
    p=i[n]
    u=p.split("=")
    t=ast.literal_eval(u[1])
    arrej.append[t]
    #r=re.sub('[a-zA-Z{=""}]','',p)
    
    #s=re.split(',',r)
    #buyInfoDict={}
    #for n in range(len(s)):
      #o=re.split(':',s[n])
      #buyInfoDict[o[0]]=int(o[1])
    #arrej.append(buyInfoDict)
  return arrej
  
  
def parseDividendInfo(mainStockArray):
  arrej=[]
  m=open('dividendInfo.py','r')
  i=m.readlines()
  
  for n in range(len(i)):
    #print("------")
    p=i[n]
    #VOD={'2018-11-28':1.27}
    
    r=re.sub('[{="":\n},]','',p)
    s=re.split("'",r)
    #['VOD', '2018-11-28', '1.27']
    
    #print('s='+str(s))
    howManyDivs=int((len(s)-1)/2)
    #print('how many divs ='+str(howManyDivs))
    
    
    divTotal=0
    #for o in range(int(howManyDivs)):
    lowerDateProtection=datetime.datetime(1,1,1).date()
    for o in range(howManyDivs):
      #print('o='+str(o))
      divName = s[0]
      divDate=datetime.datetime.strptime(s[1+(o*2)],'%Y-%m-%d').date()
      divValue = float(s[2+(o*2)])
      
      for h in range(len(mainStockArray)):
        if divName==mainStockArray[h].ticker:
          
          for z in sorted(mainStockArray[h].historyDic):
            if z<lowerDateProtection:
              pass
            else:
              if z == divDate:
                #print('Found match')
                #print('date='+str(z))
                #print('protected Date='+str(lowerDateProtection))
                lowerDateProtection=divDate
                divTotal=divTotal+divValue
                mainStockArray[h].historyDic[z][3]=divTotal
                #print('divTotal='+str(divTotal))
              else:
                #print('date='+str(z))
                #print('divTotal='+str(divTotal))
                mainStockArray[h].historyDic[z][3]=divTotal
  return mainStockArray
              
            
    
  

  
#pickle_out=open('pickle/MainStockArray.pickle','rb')
#mainStockArray=pickle.load(pickle_out)

#o=parseBuyInfoV2(mainStockArray)
  
  
  


  
  
  





