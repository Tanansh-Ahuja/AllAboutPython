#delete Dictionary Elements

dict={'a':'1','b':'2','c':'3','d':'4'}

def del_dict():
    global dict
    del dict[raw_input("Tye in the index to delete: ")]

print"Original Dictionary",dict
del_dict()
print"Altered Dictionary",dict
