class baseclass:

    def feat1():
        print('This is feature 1')

    def feat2():
        print('This is feature 2')

class derivedclass(baseclass):

    def feat3():
        print('This is feature 3')


    def feat4():
        print('This is feature 4')

#obj=baseclass
obj = derivedclass

obj.feat1()
obj.feat2()
obj.feat3()
obj.feat4()

#with this you can conclude that even when 'obj' is an object of class 'derivedclass' , even then
#it is able to use the features of base class because derived class is inheriting base class
