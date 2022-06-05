from random import *

#global variables
count=1
a=list(map(chr,map(int,range(32,127))))

#lets create a dictionary
def dict_create():
    global count
    global a 
    seed(count)
    shuffle(a)
    value=a.copy()
    shuffle(a)
    key=a.copy()
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

#main
while 1:
    b=dict_create()
    user=input("Enter: ")
    output=crypt(user)
    print(output)
