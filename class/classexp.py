class cal():


    def __init__(self,x,y):
        self.a=x
        self.b=y

    

    @classmethod
    def sm(cls):
        print('Sum is: ',cls.a+cls.b)


c=cal(2,3)
cal.sm()
