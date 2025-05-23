#in encapsulation we restrict direct access to data  
#and allow controlled interactions through functions

class person:

    __amount = 0

    def __init__(self):
        self.__amount = 0
    
    def setAmount(self,amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount    

p = person()
p.setAmount(4000)

print(p.getAmount())
# print(p._person__amount)
# we cannot modify it directly in python but we can 
#access this variable using _className__pvtvariblename 
