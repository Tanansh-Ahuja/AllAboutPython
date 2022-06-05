class one:
    
    def __init__(self,a):
        self.a=a
        

    def func1(self):
        obj = two
        print("the key is:" , self.a)
        self.a=two.change(self.a)
        print("the new key is: ",self.a)


class two:

    def change(b):
        b=b+1
        return b


#main
objct = one(1)
objct.func1()
