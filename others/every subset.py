from itertools import *
a=list(input("enter: ").split())
b=set(a)
c=b.copy()
for i in range(2,len(b)+1,1):
    c.update(set(combinations(b,i)))
print(c)
