class varobjects:

    def __init__(self,name):
        self.name=name


    def func(self):
        print('Hello',self.name)





#main
a={1:'Tanansh',2:'Bhavya'}
b=int(input('Enter your choice: '))
tempobj=varobjects(a[b])
tempobj.func()


        
