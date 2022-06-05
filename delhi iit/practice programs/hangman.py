a="askaban"
b=len(a)
x=list(a)
q=[] ; q=x ; d=[]
for j in range(0,b):
    d.append("#")

    
print("\n\t\t\t\tWelcome to the hangman game")
a=input("Enter your name: ")
print("\n\t\t\t\t\tSTART GUESSING........")
print("\n*you cant give more than 5 wrong answers")
print("\n",d)
i=5
while i>0:
    c=input("\nEnter a character: ")
    if c in x:
        print("Right anwer!!! No chance deducted!!!")
        y=x.index(c)
        d[y]=c
        x[y]="#"
        print(d)
        if d==q:
            print("\n\n\t\t\t\t\t\tYOU WIN!!!!!!")
            break
    else:
        print("WRONG CHOICE!!! ONE CHANCE DEDUCTED")
        i=i-1
        print("You are left with",i,"chances")
        if i==0:
            print("CHANCES OVER! GAME OVER")
            break
        
        
        
    
