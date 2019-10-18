import datetime
def oldestDay(floatArray):
	for stock in range(len(floatArray)):
		sample=datetime.datetime.today()
		sampleV2=datetime.datetime.strptime([f for
		f in floatArray[stock].keys()][0],'%Y-%m-%d')
		if sampleV2<sample:
			sample=sampleV2
	return sample
