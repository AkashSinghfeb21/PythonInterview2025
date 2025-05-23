'''polymorphism means one can have many forms'''
'''it refers to ovverriding and overloading in polymorphism'''
#overloading
'''in which method/func have same name 
but different arguments in same class
now python doesnt support overloading so in order to 
achieve it we will use none keyword and if else statement'''


'''class a:
   def add(self,a=None,b=None,c=None):
      if(a!=None and b!=None and c!=None):
         return a+b+c
      
      elif(a!=None and b!=None):
         return a+b
      
      else:
         return a

obj = a()

print(obj.add(1,2))'''

#overriding 
'''in which we change the functionality of functions via inheritance'''

'''class a:
    def change(self):
        print("change is temporary")

class b(a):
    def change(self):
        print("everything will be change")

o = b()

o.change()'''