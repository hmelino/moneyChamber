#https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BT.lon&apikey="apiKeyRemoved"


#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=LLOY.lon&apikey="apiKeyRemoved"

firstHalf='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol='
middleBit='BT'
lastBit='&apikey="apiKeyRemoved"'

if middleBit != 'BT':
  middleBit=middleBit+str('.LON')
full=firstHalf+middleBit+lastBit
print(full)
