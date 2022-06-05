n=int(input("Enter no. of layers: "))
for i in range(0,n,1):
    for j in range(0,i,1):
        if j%2==0:
            pass
        else:
            print(" "*(n-j),"*")
    print("")
