from random import *

#global variables

count=1
a=list(map(chr,range(32,127)))

#lets create a dictionary
def dict_create():
    global count
    global a 
    seed(count)
    shuffle(a)
    key=a.copy()
    shuffle(a)
    value=a.copy()
    final=dict(zip(key,value))
    count=count+1
    return final

#its time to crypt
def crypt(user):
    global b
    output=""
    for i in user:
        output=output+b.get(i)
    return output

def main():
    while 1:
        global b
        b=dict_create()
        user=input("Enter: ")
        output=crypt(user)
        print(output)

main()        
    
