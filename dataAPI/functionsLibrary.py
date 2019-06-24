
#create array of profits/loss for selected stock
def createFloatArray(chosenStock,dateArray,myArray,priceBought,floatArray):
	print("createFloatArray:"+str(len(floatArray)))
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
			floatArrays=floatArray
	print("dlzka vo funkcii" +str(len(floatArray)))
	return floatArrays
	


					
					
					
def priceCheck(dateArray):
	magNum=(0.5)
	for n in range(len(dateArray)-1):
		if dateArray[n]==0:
			pass
		else:
			data=float(dateArray[n+1])/float(dateArray[n])
			#print("________")
			#print("n1 = "+str(dateArray[n]))
			#print("n2 = "+str(dateArray[n+1]))
			#print("/ = "+str(data))
			#print("func "+str(dateArray[n+1])+" / "+str(dateArray[n+1]))
			if data < magNum:
				print(data)
				print("Price Anomaly")
				dateArray[n+1]=dateArray[n]
	return dateArray

# create total array
def createSumFloatArray(dezArray):
	total=0
	totalArray=[]
	for i in range(len(dezArray[0])):
		for n in range(len(dezArray)):
			total = total + dezArray[n][i]
		totalArray.append(total)
		total=0
	return totalArray



#find start date of portfolio
def startDate(mainArray):
	oldDateArray=[]
	for n in range(len(mainArray)-1):
		oldDateArray.append(mainArray[n].date)
	oldest=(sorted(oldDateArray))
	return oldest[0]
#fill array with zeros before buy
def beforeBuyDays(oldestDay,boughtAt,dateArray):
	beforeBuy=abs((oldestDay-boughtAt).days)
	for n in range(beforeBuy):
		dateArray.insert(0,0)
