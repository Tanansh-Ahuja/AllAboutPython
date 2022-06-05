while 1:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    c=input("Enter operation: ")
    if c=='+':
        print("Sum is:",a+b)
    elif c=='-':
        print("Difference is: ",a-b)
    elif c=='*':
        print("Multiplied is: ",a*b)
    elif c=="/":
        print("Division is: ",a/b)
    elif c=="p":
        print("Power is: ",a**b)
    else:
        print("Wrong input")
    n=input("do you want to enter more: ")
    if n=='y' or n=='Y':
        pass
    else:
        exit(0)
