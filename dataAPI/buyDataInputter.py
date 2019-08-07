import datetime
import pickle
import os

def openPickle():
  file=open("pickle/MainStockArray.pickle","rb")
  data=pickle.load(file)
  file.close()
  return data
  
  
def inputData(n,mainStockArray):
  print("What is the amount ? ")
  amount = input()
  print("What is the day?")
  day=input()
  if len(day)==1:
    day=str(0)+day
  print("What is the month?")
  month=input()
  if len(month)==1:
    month=str(0)+month
  print("What is the year?")
  year=input()
  date=datetime.datetime.strptime(str(day)+str(month)+str(year),"%d%m%Y").date()
  print(date)
  print("What is the cost basis?")
  price=input()
  if date and price and amount:
    arr=[]
    arr.append(amount)
    arr.append(price)
    mainStockArray[n].transactionDic[str(date)]=arr
    return mainStockArray
  
  
  


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
    



  
def buyDataInput():
  mainStockArray=openPickle()
  print("Loaded data")
  mainStockArray=addToStock(mainStockArray)
  o=open("pickle/MainStockArray.pickle","wb")
  pickle.dump(mainStockArray,o)
  o.close()
  print("Main Stock Array Saved")
 
    
#u=buyDataInput()
#ju=open("pickle/MainStockArray.pickle","rb")
#print()
#mainStockArray=pickle.load(ju)
#ju.close()

scores = {} # scores is an empty dict already

if os.path.getsize("pickle/MainStockArray.pickle") > 0:
  print("yh")
  with open("pickle/MainStockArray.pickle", "rb") as f:
    print("yh")
    unpickler = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
    scores = unpickler.load()
else:
  print(os.path.getsize("pickle/MainStockArray.pickle"))
