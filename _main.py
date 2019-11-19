from emailObject import stockList
from realTimeData import getRealTimeData
from buyInfoParse import parseBuyInfoV4, parseDividendV2
from historyProfit import historyProfit
import matplotlib
import matplotlib.pyplot as plt
from historyDic import stockFloat,HistoryPrice
from addTodaysPrices import addTodaysPrices
from etfCheck import etfCheck
import sys

msArray = stockList()
etfCheck(msArray)
parseBuyInfoV4(msArray,"buyInfo.py")
parseBuyInfoV4(msArray,"dividendInfo.py")
totalFloat=historyProfit(msArray,stockFloat)
addTodaysPrices(msArray)


def saveMsArray(msArray):
	import pickle
	pickle.dump(msArray,open("pickle/mainStockArray.pickle","wb"))
	
saveMsArray(msArray)
	
for stock in msArray:
	msArray[stock].historyDic



import numpy as np
fig=plt.figure()
ax = fig.add_subplot(1, 1, 1)
major_ticks = np.arange(0, 9000, 60)
ax.set_xticks(major_ticks)
labelsis=["Oct 18","Jan 19","Mar 19","May 19","July 19","Sep 19","Oct 19"]
ax.set_xticklabels(labels=labelsis)
plt.plot(totalFloat)
plt.axhline(0)




plt.show()
