#there are four types of inheritance in python
'''single level,multilevel,hierarchical,multiple '''

#1 single_level 
'''class a:
    def demo(self):
      print("yellow",self.__class__)

class b(a):
   pass

o = b()

o.demo()'''

#2 multi_level
'''class a:
    def demo(self):
        print("yellow",self.__class__)

class b(a):
    def run(self):
        print("running",self.__class__)

class c(b):
    pass

o2 = c()

o2.demo()
o2.run()'''

#3 hierarchical
'''class a:
    def run(self):
        print("running",self.__class__)

class b(a):
    pass

class c(a):
    pass

o =b()

o2 = c()

o.run()
o2.run()'''

#4 multiple

''' class a:
    def run(self):
        print("running",self.__class__)

class b:
    def walk(self):
        print("Walking",self.__class__)

class c(a,b):
    pass

o = c()

o.walk()
o.run()'''