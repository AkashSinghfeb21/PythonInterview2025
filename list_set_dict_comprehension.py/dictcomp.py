#ex1
num =[1,2,3,4,5]

sq_dict = dict()

for n in num:
    sq_dict[n] = n**2

print(sq_dict)    


sqdict = {n:n**2 for n in num}

print(sqdict)

#ex2

old_price = {"milk":1.02,"coffee":2.5,"bread":2.5}

new_price = {key:value*1.5 if value>2 else value for (key,value) in old_price.items()}

print(new_price)