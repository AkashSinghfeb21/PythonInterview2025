s = {1,1,2,2,3,4,5}

l = []
l.extend(s)
t = 0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            t = l[i]
            l[i] = l[j]
            l[j] = t
print(l[2])


