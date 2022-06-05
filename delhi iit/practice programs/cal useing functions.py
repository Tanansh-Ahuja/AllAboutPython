def add(x,y):
    z=x+y
    print(z)
def sub(x,y):
    z=x-y
    print(z)
def mul(x,y):
    z=x*y
    print(z)
def div(x,y):
    z=x/y
    print(z)
def pow(x,y):
    z=x**y
    return z

while 1:
    a=int(input("Enter no.1: "))
    b=int(input("Enter no.2: "))
    n=input("enter operator: ")
    if n=='+':
        add(a,b)
    elif n=="**":
        c=pow(a,b)
        print(c)
    elif n=="-":
        sub(a,b)
    elif n=='*':
        mul(a,b)
    elif n=='/':
        div(a,b)
        
