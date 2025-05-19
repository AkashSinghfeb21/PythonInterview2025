for i in range(4,0,-1):
    for j in range (0,i+1):
        print(" ",end='')
    for j in range(0,2*(4-i)+1):    
        print("*",end='')
    print("")
