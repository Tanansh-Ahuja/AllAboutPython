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


class last(derivedclass):

    def feat5():
        print('This is feature 5')


obj = derivedclass
obj1=last

obj.feat1()
obj.feat2()
obj.feat3()
obj.feat4()
#obj.feat5()                         #obj object cant be used to call feat5 function

obj1.feat1()
obj1.feat2()
obj1.feat3()
obj1.feat4()
obj1.feat5()


#with this you can conclude that even when 'obj' is an object of class 'derivedclass' , even then
#it is able to use the features of base class because derived class is inheriting base class

#also when obj1 is an object of last class it is able to use all the methods of its above inherited
#classes, this is what we call multilevel inheritence
