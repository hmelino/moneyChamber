import requests
from downloadData import oneTimeConnection
import datetime
from deposits import cashDeposits
import pickle
import sys


import matplotlib
import matplotlib.pyplot as plt
class Price:
  def __init__(self,hPrice,hAmount,fPrice,fAmount):
    self.hPrice=hPrice
    self.hAmount=hAmount
    self.fPrice=fPrice
    self.fAmount=fAmount
    
def basePriceFunc(priceObject):
  hPrice=float(priceObject.hPrice)
  hAmount=int(priceObject.hAmount)
  fPrice=float(priceObject.fPrice)
  fAmount=int(priceObject.fAmount)
    
  hTotal=hPrice*hAmount
  fTotal=fPrice*fAmount
  tTotal=hTotal+fTotal
  tAmount=hAmount+fAmount
  basePrice=tTotal/tAmount
  return basePrice
  
 

today=datetime.date.today()
portfolioTotal=2000
oldestDay=datetime.datetime.strptime("2018.10.26","%Y.%m.%d")


def indexFundCount(ticker,portfolioTotal,oldestDay):
  today=datetime.datetime.today()
  howManyDays=(today-oldestDay).days
  q=open("pickle/jsonData0.pickle","rb")
  o=pickle.load(q)
  q.close()
  #processedDate=today-dayDifference
  date=oldestDay.date()
  price=0
  arrej=[]
  totalValueOfDeposits=0
  basePrice=o['history'][str(oldestDay.date())]['close']
  multiplier=int(float(portfolioTotal)/float(basePrice))
  #basePrice=stockPrice
  priceObject=Price(0,0,0,0)
  priceObject.hPrice=basePrice
  
  
  for n in range(howManyDays):
    #dates of cash deposits
    if str(date)in cashDeposits:
      totalValueOfDeposits=totalValueOfDeposits+float(cashDeposits[str(date)])
      
      priceObject.fPrice=float(price)
      priceObject.fAmount=(totalValueOfDeposits/priceObject.fPrice)
      
      ukulele=((priceObject.hAmount*priceObject.hPrice)+(priceObject.fAmount-priceObject.hAmount)*priceObject.fPrice)/priceObject.fAmount
      basePrice=ukulele
      #print("fAmount="+str(priceObject.fAmount))
      #print("fPrice="+str(priceObject.fPrice))
      #print("hPrice="+str(priceObject.hPrice))
      #print("hAmount="+str(priceObject.hAmount))
      #print("price="+str(price))
      #print("basePrice="+str(ukulele))
      #print("---")
      
      priceObject.hPrice=ukulele
      
      
      
      
      #if priceObject.hAmount!=0:
      #basePrice=basePriceFunc(priceObject)
    
    
    
    if str(date) in o['history']:
      #count how many stocks could afford
      multiplier=int(float(totalValueOfDeposits)/float(basePrice))
      
      #index price at given date
      price=o['history'][str(date)]['close']
      #profit 
      #floatis=(float(basePrice)-float(price))*multiplier
      #print("price="+str(price))
      #print("basePrice"+str(basePrice))
      floatis=(float(price)-float(basePrice))*multiplier
      
      arrej.append(floatis)
    else:
      arrej.append(floatis)
      
    priceObject.hAmount=priceObject.fAmount
    priceObject.hPrice=priceObject.fPrice
    date=(oldestDay+datetime.timedelta(n)).date()
  print(totalValueOfDeposits)
  return arrej
  
#y=indexFundCount("VUKE",2000,oldestDay)
#plt.plot(y)

#plt.fill(y,area,facecolor='blue')
#plt.show()




