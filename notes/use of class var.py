class stud:

    seats=10
    
    def __init__(self,b,y):
        self.name=b
        self.age=y

    def printf(self):
        print(self.name,',',self.age)

    def change():
        stud.seats=stud.seats-1
        

#main

q=input("enter name: ")
w=int(input('Enter age: '))
c1=stud(q,w)
stud.change()
print("No of seats remaining: ",stud.seats)

input()


e=input("enter name: ")
r=int(input('Enter age: '))
c2=stud(e,r)
stud.change()
print("No of seats remaining: ",stud.seats)
        
c1.printf()
c2.printf()



        
        
        
