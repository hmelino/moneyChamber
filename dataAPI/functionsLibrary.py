floatArray=[]
#create array of profits/loss for selected stock
def createFloatArray(chosenStock,dateArray,myArray,priceBought):
	for n in range(len(dateArray)):
		amount=int(myArray[chosenStock].amount)
		if dateArray[n]==0:
			floatArray.append(0)
		else:
			if myArray[chosenStock].etf==True:
				iPrice=float(dateArray[n])
				bPrice=float(priceBought)*100
				profit=((iPrice-bPrice)*amount)/100
				floatArray.append(profit)
			else:
				profit=(float(dateArray[n])-float(priceBought))*amount
				floatArray.append(profit/100)
	return floatArray

#find start date of portfolio
def startDate(mainArray):
	oldDateArray=[]
	for n in range(len(mainArray)):
		oldDateArray.append(mainArray[n].date)
	oldest=(sorted(oldDateArray))
	return oldest[0]
#fill array with zeros before buy
def beforeBuyDays(oldestDay,boughtAt,dateArray):
	beforeBuy=abs((oldestDay-boughtAt).days)
	for n in range(beforeBuy):
		dateArray.insert(0,0)
