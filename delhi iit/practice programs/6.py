a=[1,2,3,4,5]
b=[]
for i in a:
    if a.index(i)%2!=0:
        i=i**2
        b.append(i)
    else:
        b.append(i)
print(b)
        
        
