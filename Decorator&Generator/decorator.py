# In Python, a decorator is a design pattern that allows you to modify 
# the functionality of a function by wrapping it in another function.
# The outer function is called the decorator, 
# which takes the original function as an argument and returns a modified version of it.

#first example without @ symbol

# def outer(func):
#     def inner():
#         print("you're under arrest")
#         func()
#     return inner 

# def original():
#     print("i am human")


# decorator = outer(original)

# decorator()

#second example with @ symbol

# def outer(func):
#     def inner():
#         print("you're under arrest")
#         func()
#     return inner

# @outer
# def original():
#     print("i am a human")

# original()    

#third example with parameters
def smartdivide(func):
    def inner(a,b):
        print("dividing",a,"and",b)
        if(b==0):
            print("sorry can't divide with zero")
            return -1
        
        return func(a,b)
    return inner    

@smartdivide
def divide(a,b):
    return a//b

print(divide(10,2))

print(divide(2,0))

