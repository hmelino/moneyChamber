def optimizeData(l):

	import numpy as np
	
	def antiAliasV2(l,steps):
		file=[np.linspace(start=l[v],stop=l[v-1],num=steps) for v in range(len(l))]
		return [x for lst in file for x in lst][steps:]
		
	def biggestDataDifferenceV2(l):
		gaps=[abs(l[v]-l[v-1]) for v in range(len(l))]
		return max(gaps[1:])
		
	def dataRange(l):
		return max(l)-min(l)
		
	def countProfitLoss(nList):
		profit=np.ma.masked_where(nList<0,nList)
		loss=np.ma.masked_where(nList>0,nList)
		return profit,loss,nList
		
	#start of optimiseData function
	minPart=dataRange(l)/100
	multiplierV2=int(biggestDataDifferenceV2(l)/10)
	
	newOne=antiAliasV2(l,multiplierV2)
	numpyList=np.array(newOne)
	return countProfitLoss(numpyList)
