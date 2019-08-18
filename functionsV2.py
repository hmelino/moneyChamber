def updateStockTotalAmount(msArray,iN):
  total=0
  for n in msArray[iN].transactionDic:
    value=(msArray[iN].transactionDic[n][0])
    total=total+value
  msArray[iN].amount=total
  
  
