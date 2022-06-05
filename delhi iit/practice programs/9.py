list_1=[]
def list_comprehension():
    global list_1
    list_1=[chr(i) for i in range(ord('a'),ord('z')+1)]

print("Calling the comprehension function...")
list_comprehension()
print("the formed list: ",list_1)
