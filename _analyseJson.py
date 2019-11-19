import os
import pickle
directory=os.fsdecode("pickle/")
arr=[]
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".pickle"):
      if filename == "realTData.pickle":
       pass
      else:
       m=open("pickle/"+str(filename),"rb")
       o=pickle.load(m)
       arr.append(o)
       m.close()
      
for r in range(len(arr)):
 try:
  print(arr[r]['name'])
  o=(arr[r]['history'].keys())
  for n in o:
   print(n)
   break
   
 except :
  pass
