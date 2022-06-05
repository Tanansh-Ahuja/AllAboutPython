from random import *

#global variables
count =1                                                                        #this is a counter for seed
a=list(map(chr,map(int,range(32,127))))                 #here i made a list of all possible characters

class __crypt__:                                                        #this class will have the function for cryting

    #dictionary create
    def dict_create():                                                      #this function will create a dictionary with every character linking to one other character
        global count                                                            #told you they were global
        global a
        seed(count)                                                             #pattern in randomness
        shuffle(a)
        key=a.copy()
        shuffle(a)
        value=a.copy()
        final=dict(zip(key,value))                                      #a dictionary is created
        count=count+1                                                       #count changes for further coading
        return final                                                            #returning to main() output variable

    #crypting time
    def crypt(user):                                                            #using the dictionary it will crypt what user entered
        global b
        global count
        output=""
        for i in user:
            output=output+b.get(i)
        f.write(output)                                                     #this will write in the created file the crypted message
        f.write("\t\t")
        f.write(str(count))                                             #you can only write string format in file not numeric
        return output

#calling everything
class main:                                                                 #a main class that contains everything
    def main():
        obj1=__crypt__                                                  #an object of class crypt to create to call functions
        while 1:                                                                # an infinite loop
            global b
            b=obj1.dict_create()                                    #callind dict_create to make a dictionary
            user=input("Enter: ")                                       #by user
            f.write("\n\n")
            f.write(user)                                                    #the original input by user goes into file
            f.write("\t\t")
            output=obj1.crypt(user)                              #calling crpyt()
            print(output)



#main
obj2=main
#since to close this program we need force stop, hence this method of file handling is used
try:
    f = open('crypting.txt','a')                                    #file opened in append mode
    f.write("\noriginal\t\tcrypted\t\tseed\n")
    obj2.main()
finally:
    f.close()

