class baseclass:

    def __init__(self):
        print('In baseclass init')

    def feat1(self):
        print('This is feature 1')

    def feat2(self):
        print('This is feature 2')

class derivedclass(baseclass):

    def __init__(self):
        print('In derivedclass init')
        super().__init__()
       

    def feat3(self):
        print('This is feature 3')


    def feat4(self):
        print('This is feature 4')

obj=derivedclass()


obj.feat1()
obj.feat2()
obj.feat3()
obj.feat4()
