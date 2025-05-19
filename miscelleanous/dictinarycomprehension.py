import re

d = {1:"a",2:"b"}

d = {v for k,v in d.items() if k%2==0}

x = str(d)

print(re.sub("[^a-zA-Z]","",x))