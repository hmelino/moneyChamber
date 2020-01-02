import pickle  
msArray=pickle.load(open('pickle/msArray.pickle','rb'))
import datetime

def withinYear(date:str):
    '''Check if provided string format date is not older than 365 days from today'''
    print(f'imported date is {date}')
    if date == '0':
        return False
    cDate=datetime.datetime.strptime(date,'%Y-%m-%d').date()
    today=datetime.datetime.today().date()
    if (today-cDate).days > 365:
        return False
    return True

def countStocksYeld():
    '''Count dividend yeld for each stock in msArray based on dividend payout in last 365 days '''
    dividendLib={}
    for stock in msArray:
        payouts = []
        for date in msArray[stock].dividendInfo.keys():
            if withinYear(date) == True:
                divPayment=(msArray[stock].dividendInfo[date])
                divident=divPayment/msArray[stock].historyDic[date].amount
                payouts.append(divident)
        yeld=sum(payouts)/msArray[stock].price
        dividendLib[stock]=yeld*100

            



q=0
