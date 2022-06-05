#Method Resolution Operator(MRO)

class baseclass:

    def __init__(self):
        print('In baseclass init')

    def feat1(self):
        print('This is feature 1')

    def feat2(self):
        print('This is feature 2')

class base2class:

    def __init__(self):
        print('In base2class init')

    def feat3(self):
        print('This is feature 3')


    def feat4(self):
        print('This is feature 4')

class lastclass(base2class,baseclass):

    def __init__(self):
        print('In lastclass init')
        super().__init__()

    def feat5(self):
        print('This is feature 5')

obj=lastclass()


obj.feat1()
obj.feat2()
obj.feat3()
obj.feat4()
obj.feat5()
