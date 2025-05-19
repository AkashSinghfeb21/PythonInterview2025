from math import sqrt

#ex1
num = []

for i in range(1,6):
    num.append(2**i)

print(num)    


numbers = [2**i for i in range(1,6)]

print(numbers)


#ex2
l = [49,64,81,100]

l_new = [sqrt(i) for i in l if i%2==0]

print(l_new)

#ex3

t1 = ["raja","chicken","milk"]
t2 = ["John","paneer","butter"]

n_l = [(x,y) for x in t1 for y in t2]

print(n_l)
