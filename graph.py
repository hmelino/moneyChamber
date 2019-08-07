import matplotlib
import matplotlib.pyplot as plt
def createGraph(dataArrayOrDic):
	floatArray=[]
	if str(type(dataArrayOrDic)) == "<class 'list'>":
		print('its array')
		floatArray=dataArrayOrDic
	else str(type(dataArrayOrDic)) == "<class 'dict'>":
		print('its dictionary')
		floatArray=[]
		for n in dataArrayOrDic.values():
			floatArray.append(n)
			
	plt.plot(floatArray)
	plt.axhline(0, color='lightseagreen')
	plt.show()
	#<class 'dict'>
	%<class 'list'>
