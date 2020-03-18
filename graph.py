def showGraphV2(self):
		def findMultiplier(array):
			result=[]
			for n in range(len(array))[1:]:
				difference = abs(array[n-1]-array[n])
				result.append(difference)
			longestLine=max(result)
			return int(longestLine/15)

		def antialias(array,multiplier):
			result=[]
			for n in range(len(array))[1:]:
				start=array[n-1]
				stop=array[n]
				step=(stop-start)/(multiplier+1)
				result.append(start)
				for _ in range(multiplier):
					start+=step
					result.append(start)
			result.append(array[-1])
			return result

		def showMonths():
			#list with first day of month index N
			fDayPositions=[]
			pDates=list(self.dayTotals.keys())
			for day in range(len(pDates)):
				if pDates[day][8:10]=='01':
					fDayPositions.append(day)
			fDayPositionsX=[v*multiplier for v in fDayPositions]
			for n in fDayPositionsX:
				plt.axvline(n,color='white',alpha=0.1)
		
		def showYears():	
			nYPositions={}
			pDates=list(self.dayTotals.keys())
			savedYear=pDates[0][0:4]
			y=min(loss)-5
			for d in range(len(pDates)):
				if pDates[d][0:4]!=savedYear:
					savedYear=pDates[d][0:4]
					nYPositions[savedYear]=d
			for year in nYPositions.keys():
				x=nYPositions[year]*multiplier
				plt.axvline(x,color='white',alpha=0.5)
				plt.annotate(year,xy=(x+200,y))

		def dividendGraph():
			dividendPlotData=[]
			for day in self.totalDividendsDict.keys():
				for _ in range(int(multiplier+1)):
					dividendPlotData.append(self.totalDividendsDict[day])
			return dividendPlotData[multiplier:]
		
		import numpy as np
		from matplotlib import pyplot as plt
		import itertools
		self.finaliseData()
		#Decorations
		dValues=list(self.dayTotals.values())
		plt.rc('axes', facecolor='#304154', edgecolor='#304154')
		plt.rc('figure',facecolor='#304154',edgecolor='#304154')
		plt.rc('savefig',facecolor='#304154',edgecolor='#304154')
		plt.rc('text',color='white')
		plt.rc('xtick',color='#304154')
		plt.rc('ytick',color='white')
		plt.rc('patch',edgecolor='white')
		#Create graph values
		multiplier=findMultiplier(dValues)
		normal=np.array(antialias(dValues,multiplier))
		profit=np.ma.masked_where(normal<0,normal)
		loss=np.ma.masked_where(normal>0,normal)
		showMonths()
		showYears()
		plt.plot(profit, color = '#96C099',label='Profit')
		plt.plot(loss, color = '#C54E59',label='Loss')

		#Dividends
		if len(self.dividendData)>1:
			dividends=dividendGraph()
			dividendsX=np.arange(0,len(dividends))
			divShadow=[normal[iN]-dividends[iN] for iN in range(len(profit))]
			plt.plot(divShadow, color='white',alpha=0.1)
			plt.fill_between(dividendsX,normal,divShadow,color='white', alpha=0.05,label='Dividends')
		plt.legend()
		plt.show()
