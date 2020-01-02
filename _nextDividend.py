import firebase
from firebase import firebase
import pickle
import datetime


def nextDividend(ticker,amount):
  today = datetime.date.today()
  furebase=firebase.FirebaseApplication('personalFirebaseServer', None)
  o=furebase.get("/"+str(ticker),None)
  dateArray=[]
  for n in o.keys():
    dateArray.append(n)
  p=(o[dateArray[0]]['payDate'])
  dividendAmount=(float(o[dateArray[0]]['divAmount']))*amount
  payDate=datetime.datetime.strptime(p,"%d%m%Y").date()
  howManyDays=(payDate-today).days
  currency=
  if howManyDays>0:
    print("In next "+str(howManyDays)+" days you will recieve £"+str(round(dividendAmount,2))+" from "+str(ticker))
  
divArray=[]
zum=open("pickle/mainStockArray.pickle","rb")
mainStockArray=pickle.load(zum)
zum.close()




 
furebase=firebase.FirebaseApplication('personalFirebaseServer', None)
for n in mainStockArray:
  name=n.ticker
  o=furebase.get("/"+str(name),None)
  if o:
    amount=int(n.amount)
    nextDividend(name,amount)
print("Over")

  
