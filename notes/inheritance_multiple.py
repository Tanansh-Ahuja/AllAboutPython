class baseclass:

    def feat1():
        print('This is feature 1')

    def feat2():
        print('This is feature 2')

class base2class:

    def feat3():
        print('This is feature 3')


    def feat4():
        print('This is feature 4')


class last(baseclass,base2class):

    def feat5():
        print('This is feature 5')


obj1=last


obj1.feat1()
obj1.feat2()
obj1.feat3()
obj1.feat4()
obj1.feat5()


