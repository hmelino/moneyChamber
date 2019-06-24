import dezArray
from dezArray import *
import graph
from graph import *
data = dezArray.demdata
totalArray=[]
#print(data[1])
print(len(data[0]))
#13
#224

total=0


for i in range(len(data[0])):
	for n in range(len(data)):
		total = total + data[n][i]
	totalArray.append(total)
	total=0
	
print(totalArray)
graph.createGraph(data[12])
		

