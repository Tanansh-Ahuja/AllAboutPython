import random

list_1=[]
def list_comprehension():
    global list_1
    list_1=[chr(i) for i in range(ord('a'), ord('z') + 1)]

print "Calling The comprehension function..."
list_comprehension()
print "The Formed list: ",list_1
