class car:
     
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
        print('In the init')

    def printf(self):
        print(self.brand,',',self.year)

#main
c1=car('BMW',2019)
#c2=car('MARUTI',2018)

#c1.printf()
#c2.printf()


        
        
        
