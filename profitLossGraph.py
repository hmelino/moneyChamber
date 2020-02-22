def optimizeData(list):

	import numpy as np
	def antiAlias(l,steps):
		#adds x amount of midpoints/steps into list
		newList=[]
		for n in range(len(l)):
			newList.append(l[n])
			try:
				for t in range(1,steps+1):
					d=(l[n+1]-l[n])/(steps+1)
					newList.append(l[n]+d*t)
			except IndexError:
				pass
		return newList
		
	def biggestDataDifference(list):
		#find longest line in plot
		biggestDifference=0
		for d in range(len(list)):
			try:
				difference=abs(list[d]-list[d-1])
				if biggestDifference<difference:
					biggestDifference=difference
			except IndexError:
				pass
		return biggestDifference
	
	def dataRange(list):
		return max(list)-min(list)
		
	def countProfitLoss(nList):
		profit=np.ma.masked_where(nList<0,nList)
		loss=np.ma.masked_where(nList>0,nList)
		return profit,loss,nList
		
	#start of optimiseData function
	minPart=dataRange(list)/100
	multiplier=int(biggestDataDifference(list)/minPart)
	newList=antiAlias(list,multiplier)
	numpyList=np.array(newList)
	return countProfitLoss(numpyList)
