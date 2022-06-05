from random import *

#global variables
count =1
a=list(map(chr,map(int,range(32,127))))

class __crypt__:
    #dictionary create
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

    #crypting time
    def crypt(user):
        global b
        global count
        output=""
        for i in user:
            output=output+b.get(i)
        f.write(output)
        f.write("\t\t")
        f.write(str(count))
        return output

#calling everything
class main:
    def main():
        obj1=__crypt__
        while 1:
            global b
            b=obj1.dict_create()
            user=input("Enter: ")
            f.write("\n")
            f.write(user)
            f.write("\t\t")
            output=obj1.crypt(user)
            print(output)
#main
obj2=main
try:
    f = open('decrypting.txt','a')
    f.write('\nCode\t\tOriginal\t\tSeed\n')
    obj2.main()
finally:
    f.close()

