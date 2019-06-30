class Stock (object):
	def __init__(self,name, price):
		self.name=name
		self.price=price
		
class BoughtDate (object):
	def __init__(self,date,amount):
		self.date=date
		self.amount=amount
		
ztock=Stock("vuke",52.4)
msti=BoughtDate("11.2.2019",7)
ztock.oko=msti
print(ztock.oko.date)
	
