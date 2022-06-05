def addel(a):
    i=input("Enter the element: ")
    a.append(i)

q=[]
while 1:
    ans=input("Do you want to add an element?")
    if ans=='y':
        addel(q)
    else:
        exit(0)
    print(q)
    
