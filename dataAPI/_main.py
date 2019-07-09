import downloadData
import emailData
from emailData import *
import emailObject
from emailObject import *
from downloadData import *
import json
import historyData
from historyData import *
import functionsLibrary
from functionsLibrary import *
import datetime
import operator
import matplotlib
import matplotlib.pyplot as plt
import buyInfoParse
from buyInfoParse import *
import dividendInfo
from dividendInfo import *
import buyInfo 
from buyInfo import *
import sys 
import offlineData
from offlineData import *
import createStockData
from createStockData import *



start = time.time()
	
############################################################################################################################################         start of program

#check is MainStockArray is saved
mainStockArray=functionsLibrary.isMainStockArraySaved()
  
#check date of saved Data
functionsLibrary.checkDateOfSavedData(mainStockArray)
  
 
#Process mainStockArray
buyInfo=buyInfoParse.parseBuyInfo(mainStockArray)
dictionary={}
for n in range(len(buyInfo)):
  mainStockArray[n].transactionDic=buyInfo[n]
mainStockArray=functionsLibrary.multipyETFprice(mainStockArray)
dateArray=functionsLibrary.dateArray(mainStockArray)
mainStockArray=buyInfoParse.parseDividendInfo(mainStockArray)
floatArray=[]



#check if floatArray exist

try:
  pickle_floatArray=open("pickle/floatArray.pickle","rb")
  floatArray=pickle.load(pickle_floatArray)
  pickle_floatArray.close()
  print("Found saved floatArray")
except :
  print("floatArray is not created yet")
  for n in range(14):
    o=createStockData.createData(n,mainStockArray)
    floatArray.append(o)
    
  print("Downloaded and processed all data")
  print("Creaed float Array")
  
  pickle_floatArrayOut=open("pickle/floatArray.pickle","wb")
  pickle.dump(floatArray,pickle_floatArrayOut)
  pickle_floatArrayOut.close()
  print("Saved Float Data")
  #end



  



zfloat=[]
for day in range(len(floatArray[0])):
  data=0
  for array in floatArray:
    data=float(array[day])+data
  zfloat.append(data)


plt.plot(zfloat)
plt.axhline(0, color='lightseagreen')
plt.show()

functionsLibrary.saveMainStockArray(mainStockArray)


namesArray=[]

for n in range(len(mainStockArray)):
  namesArray.append(mainStockArray[n].ticker)
print(namesArray)


  








end = time.time()
print(end-start)




		





