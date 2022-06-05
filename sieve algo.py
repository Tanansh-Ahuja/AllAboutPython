from math import sqrt
n=100
#n= int(input('Enter a no: '))
'''
# Basic sieve algorithm
#i need to find all prime nos till n
loprime=[]
for i in range(n+1):
    loprime.append(True)

for i in range(2,n+1):
    if loprime[i]==True:
        j=2
        while j*i<=n:
            loprime[i*j]=False
            j=j+1
l=n+1
final=[]
for i in range(l):
    if loprime[i]:
        final.append(i)
print(final)
'''    

#My approch to it
lop=[]
lon=list(range(n+1))
i=2
while i<=sqrt(n):
    if lon[i]!=0:
        lop.append(lon[i])
        j=i
        while j*i<=n:
            lon[j*i]=0
            j=j+1
    i=i+1
print(lop)
print(lon)
'''c=0
for i in lon:
    if i!=0:
        c=c+1
print(c)
'''
