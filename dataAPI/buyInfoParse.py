
import buyInfo
from buyInfo import *
import sys
import re


def parseBuyInfo():
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
  
  
  


  
  
  





