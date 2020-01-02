
import buyInfo
from buyInfo import *
import dividendInfo
from dividendInfo import *
import ast

def parseBuyInfoV4(msArray,source:str()):
	data = {f.split("=")[0]:ast.literal_eval(f.split("=")[1]) for f in open(source,'r').readlines()}
	if source=="dividendInfo.py":
		for f in data:
			msArray[f].dividendInfo=data[f]
	else:
		for f in data:
			msArray[f].buyInfo=data[f]
