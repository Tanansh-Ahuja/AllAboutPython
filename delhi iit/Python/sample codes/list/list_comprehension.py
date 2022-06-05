import random

list_1=[]
def list_comprehension():
    global list_1
    list_1=[random.randint(1,x) for x in range(10,100)]

print "Calling The comprehension function..."
list_comprehension()
print "The Formed list: ",list_1
