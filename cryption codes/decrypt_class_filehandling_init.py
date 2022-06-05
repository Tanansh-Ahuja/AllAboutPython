from random import *

class __crypt__:                                                        #this class will have the function for cryting

    def __init__(self,argcount,arga):
        self.count=argcount
        self.a=arga

    #dictionary create
    def dict_create(self):                                                      #this function will create a dictionary with every character linking to one other character
        seed(self.count)                                                             #pattern in randomness
        shuffle(self.a)
        value=self.a.copy()
        shuffle(self.a)
        key=self.a.copy()
        final=dict(zip(key,value))                                      #a dictionary is created
        self.count=self.count+1                                                       #count changes for further coading
        return final                                                            #returning to main() output variable

    #crypting time
    def crypt(self,user,b):                                                            #using the dictionary it will crypt what user entered
        output=""
        for i in user:
            output=output+b.get(i)
        f.write(output)                                                     #this will write in the created file the crypted message
        f.write("\t\t")
        f.write(str(count))                                             #you can only write string format in file not numeric
        return output

#calling everything
class main:                                             #a main class that contains everything

    def __init__(self1,argcount,arga):
        self1.count=argcount
        self1.a=arga
        
    def main(self1):
        obj1=__crypt__  (self1.count,self1.a)                                                #an object of class crypt to create to call functions
        while 1:                                                                # an infinite loop
            b=obj1.dict_create()                                    #callind dict_create to make a dictionary
            user=input("Enter: ")                                       #by user
            f.write("\n\n")
            f.write(user)                                                    #the original input by user goes into file
            f.write("\t\t")
            output=obj1.crypt(user,b)                              #calling crpyt()
            print(output)

#main
count =1
a=list(map(chr,map(int,range(32,127))))
obj2=main(count,a)
#since to close this program we need force stop, hence this method of file handling is used
try:
    f = open('decrypting2.txt','a')                                    #file opened in append mode
    f.write("\noriginal\t\tcrypted\t\tseed\n")
    obj2.main()
finally:
    f.close()

