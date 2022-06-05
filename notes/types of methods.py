class student:
    school='CSOFT'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3


    @classmethod                 #this is a decorator
    def info(c1):
        return c1.school


    @staticmethod               #this is a static method
    def thisclass():
        print('This is student class.')


#main
s1=student(34,45,67)
s2=student(44,89,78)

print(s1.avg())
print(s2.avg())
print(student.info())

student.thisclass()


    
