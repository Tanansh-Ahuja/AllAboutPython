class car:

    wheels=4
    
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def printf(self):
        print(self.brand,',',self.year,',',self.wheels)
        #self.wheels=self.wheels+1

#main
c1=car('BMW',2019)
c2=car('MARUTI',2018)

c1.printf()
c2.printf()


        
        
        
