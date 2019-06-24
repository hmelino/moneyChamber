import AV
from AV import *
import BT
from BT import *
import CREI
from CREI import *
import EVR
from EVR import *
import HL
from HL import *
import INVP
from INVP import *
import LLOY
from LLOY import *
import MKS
from MKS import *
import PSN
from PSN import *
import PTEC
from PTEC import *
import VMID
from VMID import *
import VOD
from VOD import *
import VUKE
from VUKE import *
import matplotlib
import matplotlib.pyplot as plt
import sys 

def createGraph(dataArray):
	plt.plot(dataArray)
	plt.show()

AV1=AV.demdata
BT1=BT.demdata
CREI1=CREI.demdata
EVR1=EVR.demdata
HL1=HL.demdata
INVP1=INVP.demdata
LLOY1=LLOY.demdata
MKS1=MKS.demdata
PSN1=PSN.demdata
PTEC1=PTEC.demdata
VMID1=VMID.demdata
VOD1=VOD.demdata
VUKE1=VUKE.demdata

def priceAnomaly(dateArray):
	for n in range(len(dateArray)-1):
		print(type(dateArray[0]))
		if int(dateArray[n]) & int(dateArray[n+1] )!=0:
			data=abs(float(dateArray[n+1]))/abs(float(dateArray[n]))
			if data > 30:
				print("Price Anomaly")
				dateArray[n+1]=dateArray[n]
	m=open("CREI2.py","a+")
	m.write("demData="+str(dateArray))
	m.close
	return dateArray
		
data=priceAnomaly(CREI1)
print(data)
createGraph(data)


