import datetime
import pickle
import os

def openPickle():
  file=open("pickle/MainStockArray.pickle","rb")
  data=pickle.load(file)
  file.close()
  return data
  
def findStock(chosenStock):
  for n in range(len(mainStockArray)):
    indexNum=None
    found=False
    if chosenStock in (mainStockArray[n].ticker):
      indexNum=n
      found=True
      break
  if found==True:
    return indexNum
  else:
    return False
  


def addToStock(mainStockArray):
  msArray=[]
  print("Please enter name of Stock")
  ticker=input()
  for n in range(len(mainStockArray)):
    if mainStockArray[n].ticker == ticker:
      print("Match")
      return inputData(n,mainStockArray)
      break
    elif n == len(mainStockArray)-1 and mainStockArray[n].ticker != ticker:
      print("No match")
    



  

  
 
    
#u=buyDataInput()
ju=open("pickle/MainStockArray.pickle","rb")
#mainStockArray=pickle.load(ju)
#ju.close()




mainStockArray=openPickle()
print("Loaded data")
print("What is the name of Stock ? ")
ticker=input()
indexNum=False
stockName=findStock(ticker)
if stockName != False:
  indexNum=stockName
  print("Found stock "+str(ticker))
  print(indexNum)
  print("What is the amount ? ")
  amount=input()
  print("what is the day ? ")
  day=input()
  print("what is the month ? ")
  month=input()
  print("what is the year ? ")
  year=input()
  date=(year+"-"+month+"-"+day)
  if date in mainStockArray[indexNum].transactionDic:
  
    print("You are about to adjust data of "+str(mainStockArray[indexNum].transactionDic[date])+" shares")
    print("What is the Execution price ?")
    exPrice=input()
    arr=[]
    arr.append(amount)
    arr.append(exPrice)
    print("Updating dictionary")
    d={date:arr}
    dictionary=mainStockArray[indexNum].transactionDic
    dictionary.update(d)
    print("Finished")
    
  else:
    print("new one")

    
  

