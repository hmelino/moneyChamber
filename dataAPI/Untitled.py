class User:
   """
   Custom User Class
   """
    def __init__(self,name,age,active,balance,other_names,friends,spouse):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.other_names = other_names
        self.friends = friends
        self.spouse = spouse
        
    def __str__(self):
        return self.name
p=Us
