import emailObject
from emailObject import stockList
import datetime
import realTimeData
from realTimeData import getRealTimeData
import buyInfoParse
from buyInfoParse import parseBuyInfoV4, parseDividendV2
import pickle
import matplotlib
import matplotlib.pyplot as plt
import oldestDay
from oldestDay import oldestDay
import historyDic
from historyDic import stockFloat,HistoryPrice
import requests

def etfCheck():
	etfArray=["VUKE","VMID"]
	for stock in msArray:
		if stock in etfArray:
			msArray[stock].etf=True
		else:
			msArray[stock].etf=False
	


msArray = stockList()
etfCheck()
parseBuyInfoV4(msArray,"buyInfo.py")
parseBuyInfoV4(msArray,"dividendInfo.py")

floatArray=[]
for stockName in msArray:
	q=stockFloat(stockName,msArray)
	floatArray.append({f:msArray[stockName].historyDic[f].profit for f in msArray[stockName].historyDic})
	
oldestDay=oldestDay(floatArray)
totalFloat=[]
today=datetime.datetime.today().date()
portfolioOwned=(today-oldestDay.date()).days
for day in range(portfolioOwned):
	processedDay=str((oldestDay + datetime.timedelta(day)).date())
	print(processedDay)
	dayTotal=0
	for stock in msArray:
		if processedDay in msArray[stock].historyDic:
			dayTotal+=msArray[stock].historyDic[processedDay].profit
	totalFloat.append(dayTotal)



jsonData=requests.get('"secretWebsiteForRealTimeData"').json()
namesArray=[f for f in msArray]


resultDicV2={jsonData[q]['name']:jsonData[q]['price']['buy'] for q in range(len(jsonData)) if jsonData[q]['name'] in namesArray and jsonData[q]['margin']==1}




stock="VMID"
selectedStock=[msArray[stock].historyDic[f].profit for f in msArray[stock].historyDic]
plt.plot(selectedStock)




#plotting
plt.axhline(0)
plt.show()
		



	


"""
def createStockFloatV2(iN, msArray, realTData):
  etf = msArray[iN].etf
  ticker = msArray[iN].ticker
  today = datetime.date.today()
  periodOwned = today - msArray[iN].date
  print("Processing "+str(ticker))
  try:
    io = open("pickle/jsonData" + str(iN)+ ".pickle", "rb")
    jsonData = pickle.load(io)
    io.close()
    try:
     jsonData['history'][yesterday]['close']
     print("One day old data")
    except:
     jsonData['history'][twoDaysAgo]['close']
     print("Two days old data")
  except:
    jsonData = oneTimeConnection(msArray[iN].ticker)
    yu = open("pickle/jsonData"+str(iN)+".pickle", "wb")
    pickle.dump(jsonData, yu)
    yu.close()
    
  price = realTData.data[ticker]
  if etf == False:
    price = round(float(price) / 100, 4)

  parseBuyInfoV3(msArray)
  parseDividendV2(msArray)
  updateStockTotalAmount(msArray, iN)

  mainDic = {}
  amountUpdate(msArray)
  totalAmount = int(msArray[iN].amount)
  amount = 0
  oldestDay=msArray[iN].date
  ownedFor=int((today-oldestDay).days)
  price=realTData.data[str(ticker)]
  amount=0
  amountBackup=0
  basePrice=0
  basePriceBackup=0
  dividend=0
  if etf==False:
    price=price/100
    
  for n in range(ownedFor):
    arrej=[]
    processedDate=oldestDay+datetime.timedelta(n)
    #update price if found in jsonData
    if str(processedDate) in jsonData['history']:
      price=round(float(jsonData['history'][str(processedDate)]['close']),3)
      if etf == False:
        price=price/100
        price=round(price,3)
      
    #update amount & basePrice if found
    if str(processedDate) in msArray[iN].transactionDic:
      amount=amount+int(msArray[iN].transactionDic[str(processedDate)][0])
      basePrice=msArray[iN].transactionDic[str(processedDate)][1]
      
      if etf == False:
        basePrice=basePrice/100
        
      todayTotal=amount*basePrice
      yesterdayTotal=amountBackup*basePriceBackup
      total=todayTotal+yesterdayTotal
      amountTotal=amount+amountBackup
      #value to be added to dic
      basePrice=round((total/amountTotal),3)
      #save values for future use
      amountBackup=amount
      basePriceBackup=basePrice
    #update dividend if found
    if str(processedDate) in msArray[iN].dividendDic:
     dividendis=(msArray[iN].dividendDic[str(processedDate)])
     dividend=dividendis+dividend
    floatisWD=round(((price-basePrice)*amount)+dividend,3)
    floatisND=round(((price-basePrice)*amount),3)
    
    
    arrej.append(price)
    arrej.append(amount)
    arrej.append(basePrice)
    arrej.append(dividend)
    arrej.append(floatisWD)
    arrej.append(floatisND)
    mainDic[str(processedDate)]=arrej
  msArray[iN].historyDic=mainDic
  return jsonData




for n in range(len(msArray)):
  createStockFloatV2(n, msArray, realTData)

#save msarray after filling it up with data
msSave=open("pickle/mainStockArray.pickle","wb")
pickle.dump(msArray,msSave)
msSave.close()


def theOldestDay(msArray):
  theOldestDay=datetime.date.today()
  for n in range(len(msArray)):
    date=msArray[n].date
    if date < theOldestDay:
      theOldestDay=date
  return theOldestDay
old=theOldestDay(msArray)

howLong=(datetime.date.today()-old).days

"""
oldestDay=oldestDay(floatArray)
portfolioOwned=(today-oldestDay.date()).days
finalArray=[]
for y in range(portfolioOwned):
  datey=oldestDay+datetime.timedelta(y)
  value=0
  
  for n in range(len(msArray)):
    if str(datey) in msArray[n].historyDic:
      
      o=msArray[n].historyDic[str(datey)][4]
      value=value+o
  finalArray.append(round(value,4))

"""



  
# todays data into finalArray
todaysFloat=0
for n in range(len(msArray)):
 m=(msArray[n].historyDic[yesterday])
 rTData=realTData.data[msArray[n].ticker]
 q=(rTData-m[2])*m[1]
 todaysFloat=todaysFloat+q
 #msArray[0].historyDic['2019-09-10']
todaysFloat=round(todaysFloat+divsArray[-1],3)
finalArray.append(todaysFloat)
  
  
indexF=indexFundCount
plt.plot(finalArray, color="green")
plt.plot(divsArray, color="blue")
plt.axhline(0, color='blue')
plt.plot(indexFund.indexFundCount("VUKE",2000,indexFund.oldestDay), color='#a327ff')
plt.show()
timeFinish=datetime.datetime.now()
ooo=(timeFinish-timeStart).microseconds
print(ooo/1000000)



#finalPrint
printFormat=(' {:>7}|{:^8}| {:^7}|{:^5}|{:^7}')
print(str(printFormat).format("ticker","amount","status","div","profit"))
for n in range(len(msArray)):
 yeld=round((msArray[n].historyDic[yesterday][4]/(msArray[n].historyDic[yesterday][2]*msArray[n].historyDic[yesterday][1]))*100,2)
 print(str(printFormat).format(msArray[n].ticker,msArray[n].amount,round(msArray[n].historyDic[yesterday][4],1),round(msArray[n].historyDic[yesterday][3],1),str(yeld)+"%"))
 
 #print(str(printFormat).format("",
accTotal=0
for n in range(len(msArray)):
 m=msArray[n].historyDic[yesterday]
 accTotal+=round((m[2]*m[1])+m[3],2)
 

 
print("-----------------------------------------")
print(str(printFormat).format(" ","£"+str(round(accTotal,2)),"£ "+str(round(finalArray[-1],2)),divsArray[-1],str(round((finalArray[-1]/accTotal)*100,2))+"%"))

"""





 





