import pickle
import functionsLibrary
from functionsLibrary import *
import buyInfoParse
from buyInfoParse import *
import matplotlib
import matplotlib.pyplot as plt

chosenStock=0
try:
  pickle_MainStockArray=open("pickle/MainStockArray.pickle","rb")
  mainStockArray=pickle.load(pickle_MainStockArray)
  pickle_MainStockArray.close()
  print("Found MainStockArray file")
except :
  print("MainStockArray is not created yet")
  sys.exit()
buyInfo=buyInfoParse.parseBuyInfo(mainStockArray)
dictionary={}
for n in range(len(buyInfo)):
  mainStockArray[n].transactionDic=buyInfo[n]
  
dateArray=functionsLibrary.dateArray(mainStockArray)



#create Float Array
uArray=functionsLibrary.createFloatArrayV2(mainStockArray,dateArray,True)
#uArray=functionsLibrary.fixLast0(uArray)

uArrayRaw=functionsLibrary.createFloatArrayV2(mainStockArray,dateArray,False)
#uArrayRaw=functionsLibrary.fixLast0(uArrayRaw)

plt.plot(uArray[0])
plt.axhline(0, color='lightseagreen')
today=datetime.date.today()
chosenStock=0
plt.axhline(mainStockArray[chosenStock].historyDic[today][3],color='#054f87')
plt.show()
  
  
