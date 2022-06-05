def arcircle():
    r=int(input("Enter radius: "))
    print("Area: ", 3.14*r*r)
def prec():
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    print("Perimeter: ",2*l+2*b)
def ke(m,v):
    print("Kinetic energy: ",0.5*m*v*v)

while 1:
    print("\n1. Circle\n2.Rectangle\n3.K.E.")
    n=int(input("Enter your choice: "))
    if n==1:
        arcircle()
    elif n==2:
        prec()
    elif n==3:
        m=int(input("Enter mass: "))
        v=int(input("Enter velocity: "))
        ke(m,v)
