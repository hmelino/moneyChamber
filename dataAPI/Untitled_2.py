import Untitled_1
from Untitled_1 import Stock
import pickle
myObj=Stock("VUKE",8,5,{},6,True,4,2)


pickle_out=open("hdjd.pickle","wb")
pickle.dump(myObj,pickle_out)
pickle_out.close()

pickle_in=open("hdjd.pickle","wb")
pickle.load(pickle_in)

