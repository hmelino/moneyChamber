demData=[0,0,0,0,0,0,0,5.9,5.7,5.4,5.6,-185,-187,-184,4.2,5.8,5.9]
magNum=(-20)


for n in range(len(demData)-1):
	if demData[n]==0:
		pass
	else:
		data=demData[n+1]/demData[n]
		if data < magNum:
			print(data)
			demData[n+1]=demData[n]
print(demData)
		
				
	
