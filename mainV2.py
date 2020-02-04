class MoneyChamber:
    db={}
    class Stock:
        def __init__ (self,l):
            self.date=l[2]
            self.buySell=l[3]
            self.amount=l[4]
            self.name=l[5]


    def loadStatement(self,url):
        data=open(url,'r').readlines()
        result = [l.split('\t') for l in data]
        for d in result:
            self.db[d[5]]=self.Stock(d)
        return result

        
        
o=MoneyChamber()
p=o.loadStatement('statementV2.txt')
print(p)
pass
