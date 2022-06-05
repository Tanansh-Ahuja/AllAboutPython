def delelement(a):
    n=int(input("Enter the index you want to delete: "))
    del a[n-1]

b=[1,3,4,'hyyt',678]
while 1:
    print(b)
    ans=input("Do you want to delete: ")
    if ans=='y':
        delelement(b)
    else:
        exit(0)
        
