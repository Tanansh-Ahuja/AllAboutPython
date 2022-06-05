#this creates a iterable. to show you how they work
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
#This is a function like range. just coded by me
class MyGen():
    current=0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current +=1
            return num
        raise StopIteration

gen = MyGen(0,100)
for i in gen:
    print(i)

#main
special_for([1,2,3,4])

