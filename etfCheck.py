def etfCheck(msArray):
	etfArray=["VUKE","VMID"]
	for stock in msArray:
		if stock in etfArray:
			msArray[stock].etf=True
		else:
			msArray[stock].etf=False
