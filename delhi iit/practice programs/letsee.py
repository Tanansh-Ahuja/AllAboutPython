a='yourname'
a=a.upper()
c=a[0]
b=len(a)
for i in range(1,len(a)+1,1):
    print(" "*(b),c)
    c=" "+c+a[i]
    c=a[i]+c
    b=b-1
