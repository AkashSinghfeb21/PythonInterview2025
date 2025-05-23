#in abstraction we hide implementation and 
#focus on only functionality

from abc import ABC,abstractmethod

class a(ABC):
     @abstractmethod
     def area(self):
          pass

class square(a):
     
     def __init__(self,s):
          self.s = s

     def area(self):
          return self.s*self.s 

class rectangle(a):

     def __init__(self,l,b):
          self.l = l
          self.b = b

     def area(self):
          return self.l*self.b

class circle(a):

     def __init__(self,r):
          self.r = r

     def area(self):
          return 3.14*self.r*self.r

sq = square(4)
rect = rectangle(4,5)
cir = circle(4)

print(sq.area(),"\n",rect.area(),"\n",cir.area())
      
