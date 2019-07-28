import datetime
import pickle
import emailObject
from emailObject import *
import realTimeData
from realTimeData import *

def dateArray(mainStockArray):
  oldDateArray=[]
  for n in range(len(mainStockArray)-1):
    oldDateArray.append(mainStockArray[n].date)
  oldest=(sorted(oldDateArray))
  dateArray=[]
  oldestDay=oldest[0]
  
  today=datetime.datetime.today().date()
  howLong=int((today-oldestDay).days)
  for n in range(howLong+1):
    demDay=today-datetime.timedelta(n)
    dateArray.append(demDay)
  return dateArray




def createPriceDic(ownershipPeriod,dateNow,jsonData,transactionDic):
  priceDic={}
  # create dic of prices based on how long I owned them
  priceDicValue=0
  boughtAt=0
  for n in range(int(ownershipPeriod)+1):
    demDate = dateNow-datetime.timedelta(n)
    if str(demDate) in jsonData['Time Series (Daily)']:
      priceDicValue = float(jsonData['Time Series (Daily)'][str(demDate)]['4. close'])
      priceDic[demDate]=priceDicValue
      if demDate in transactionDic:
        firstlart=float(transactionDic[demDate])/totalAmountToday
    else:
        #if date doesnt exist, put previous value
        priceDic[demDate]=priceDicValue
  return priceDic


#fix first 1 or 2 days with 0 prices
def fixZeroPriceDay(priceDic,oneDay):
  for n in priceDic:
    if priceDic[n]!=0:
      pass
    elif priceDic[n]==0 and priceDic[n-oneDay]!=0:
      priceDic[n]=priceDic[n-oneDay]
    elif priceDic[n-oneDay*2]!=0:
      priceDic[n-oneDay]=priceDic[n-oneDay*2]
      priceDic[n]=priceDic[n-oneDay]
    
  return priceDic



#create array of profits/loss for selected stock
def createFloatArray(chosenStock,dateArray,myArray,priceBought,floatArray):
	print("createFloatArray:"+str(len(floatArray)))
	for n in range(len(dateArray)):
		amount=int(myArray[chosenStock].amount)
		if dateArray[n]==0:
			floatArray.append(0)
		else:
			if myArray[chosenStock].etf==True:
				iPrice=float(dateArray[n])
				bPrice=float(priceBought)*100
				profit=((iPrice-bPrice)*amount)/100
				floatArray.append(profit)
			else:
				profit=(float(dateArray[n])-float(priceBought))*amount
				floatArray.append(profit/100)
			floatArrays=floatArray
	print("dlzka vo funkcii" +str(len(floatArray)))
	return floatArrays
	

#create floatDic from priceDic
def createFloatDic():
	floatDic={}
	boughtAt = mainStockArray[selectedStock].price
	boughtWhen = mainStockArray[selectedStock].date
	
	for n in priceDic:
		if str(n) in transactionDic:
			amount=amount-int((transactionDic[str(n)]))
			floatDic[n]=((priceDic[n]-float(boughtAt))*float(amount))/100
		else:
			floatDic[n]=((priceDic[n]-float(boughtAt))*float(amount))/100
			
	return floatDic
	
# create precious base prices
def createPreviousBasePrice(historyDic,selectedStock,mainStockArray):
	basePrice=float(mainStockArray[selectedStock].price)
	#how many times bough this stock
	transactions=int(len(mainStockArray[selectedStock].transactionDic))
	transactionDic=mainStockArray[selectedStock].transactionDic
	#transactions=int((len(vuki)))
	for n in historyDic:
	  
		previousDay=n-datetime.timedelta(1)
		price=historyDic[n][0]
		amount=int(historyDic[n][1])
		
		if str(n) in transactionDic and transactions>1:
		  # 3247*19
		  m = basePrice*amount
		  # 19-7=12
		  o = amount-(historyDic[previousDay][1])
		  #3313
		  l = (float(price))*o
		  k =m-l
		  basePrice=round((k/historyDic[previousDay][1]),1)
		  historyDic[n][2]=basePrice
		  historyDic.update
		  # to protect from out of range 
		  transactions=transactions-1
		else:
		  historyDic[n][2]=basePrice
	return historyDic



#create history dictionary
def createHistoryDic(totalAmountToday,mainStockArray,selectedStock,priceDic):
  transactionDic=mainStockArray[selectedStock].transactionDic
  historyDic={}
  amount = totalAmountToday
  #base price is fixed for now, will be adjusted later
  baseprice=mainStockArray[selectedStock].price
  
  
  for n in priceDic:
    if str(n) in transactionDic:
      historyDic[n]=[float(priceDic[n]),int(amount),float(baseprice),0]
      amount=amount-transactionDic[str(n)]
    else:
      historyDic[n]=[float(priceDic[n]),int(amount),float(baseprice),0]
  return historyDic
		
					
					
					
def priceCheck(dateArray):
	magNum=(0.5)
	for n in range(len(dateArray)-1):
		if dateArray[n]==0:
			pass
		else:
			data=float(dateArray[n+1])/float(dateArray[n])
			if data < magNum:
				print(data)
				print("Price Anomaly")
				dateArray[n+1]=dateArray[n]
	return dateArray

# create total array
def createSumFloatArray(dezArray):
	total=0
	totalArray=[]
	for i in range(len(dezArray[0])):
		for n in range(len(dezArray)):
			total = total + dezArray[n][i]
		totalArray.append(total)
		total=0
	return totalArray

#multiply ETF value by 100 
def multipyETFprice(mainStockArray):
  for n in range(len(mainStockArray)):
    if mainStockArray[n].etf == True:
      mainStockArray[n].price = float(mainStockArray[n].price)*100
      mainStockArray[n].etf = False
  return mainStockArray
	
#if price is much smaller than real , it will get multiplied by 100
def fixPriceAnomalies(mainStockArray,priceDic,selectedStock):
	  data=mainStockArray[selectedStock].price
	  for n in priceDic:
	    m=(float(data)/float(priceDic[n]))
	    if m > 50:
	      priceDic[n]=(priceDic[n])*100
	  return priceDic
	
#create array from dictionary  
def floatArrayFromDic(historyDic,dateArray):
	  #turn dictionary into array 
	  floatArray=[]
	  for n in dateArray:
	    if n in historyDic:
	      price=historyDic[n][0]
	      amount=historyDic[n][1]
	      basePrice=historyDic[n][2]
	      float=((price-basePrice)*amount)/100
	      floatArray.append(float)
	    else:
	      floatArray.append(0)
	  return floatArray[::-1]
	  
#save MainStockArray
def saveMainStockArray(mainStockArray):
  pickle_MainStockArrayOut=open("pickle/MainStockArray.pickle","wb")
  pickle.dump(mainStockArray,pickle_MainStockArrayOut)
  pickle_MainStockArrayOut.close()
  print("Saved MainStockArray pickle")
	      
# check if MainStockArray exists
def isMainStockArraySaved():
  try:
    pickle_MainStockArray=open("pickle/MainStockArray.pickle","rb")
    mainStockArray=pickle.load(pickle_MainStockArray)
    pickle_MainStockArray.close()
    print("Found MainStockArray file")
  except :
    print("MainStockArray is not created yet")
    mainStockArray=emailObject.createStockClass()
    print("----Created New Main Stock Array----")
  return mainStockArray
  
  

def checkDateOfSavedData(mainStockArray):
  print('Starting Date Check')
  todaysDate=datetime.date.today()
  todaysHour=datetime.datetime.now().hour

  #print(todaysHour)
  #print(todaysDate)
  upToDate=False
  if mainStockArray[0].timeStamp==datetime.date.today():
    print("Your saved data are up to date")
    upToDate=True
  elif mainStockArray[0].timeStamp==datetime.date.today()-datetime.timedelta(1):
      print("You have 1 day old data, gonna try dowload new ones")
      upToDate=True
      if todaysHour<8:
        print('Markets are not opened yet')
      elif todaysHour>8 and todaysHour<17:
        print('End of Day price is not ready yey')
      elif todaysHour>17:
        print('Markets are closed,gonna try dowload data')
        data=realTimeData.getRealTimeData(realTimeData.namesArray)
        print("data="+str(data))
        print("dowloaded Real Time Data")
        for n in range(len(mainStockArray)):
          #print(mainStockArray[n].ticker)
          if mainStockArray[n].ticker in data:
            pass
            yesterdaysData=mainStockArray[n].historyDic[todaysDate-datetime.timedelta(1)]
            arrej=[]
            newPrice=data[mainStockArray[n].ticker]
            if mainStockArray[n].ticker == 'VMID' or mainStockArray[n].ticker=='VUKE':
              newPrice=newPrice*100
            arrej.append(newPrice)
            arrej.append(yesterdaysData[1])
            arrej.append(yesterdaysData[2])
            arrej.append(yesterdaysData[3])
            mainStockArray[n].historyDic[todaysDate]=arrej
            print(arrej)
        mainStockArray[0].timeStamp=todaysDate
      
      
  else:
    print("Saved data are old")
    print(mainStockArray[0].timeStamp)
    upToDate=False
  return upToDate
  
def createFloatArrayV2(mainStockArray,dateArray,showDividend):
  
  uArray=[]
  dailyFloat=0
  for n in range(len(mainStockArray)):
    #separate Stocks
    gArray=[]
    for m in sorted(dateArray):
      if m in sorted(mainStockArray[n].historyDic):
        realTprice=mainStockArray[n].historyDic[m][0]
        boughtAt=mainStockArray[n].historyDic[m][2]
        amount=mainStockArray[n].historyDic[m][1]
        dividend=mainStockArray[n].historyDic[m][3]
        if showDividend==True:
          dailyFloat=(((realTprice-boughtAt)*amount)/100)+dividend
        else:
          dailyFloat=(((realTprice-boughtAt)*amount)/100)
        gArray.append(dailyFloat)
      else:
        gArray.append(0)
    uArray.append(gArray)
  return uArray
  
  
#fix if last number is 0
def fixLast0(black):
  for n in range(len(black)-1):
    if black[n] == 0:
      print("found mistake")
      black=black[:n]
  return black

	    


def beforeBuyDays(oldestDay,boughtAt,dateArray):
	beforeBuy=abs((oldestDay-boughtAt).days)
	for n in range(beforeBuy):
		dateArray.insert(0,0)
