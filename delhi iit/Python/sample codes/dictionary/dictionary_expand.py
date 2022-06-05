#Add Dictionary Elements

dict={'a':'1','b':'2','c':'3','d':'4'}
ar_key=['e','f','g','h']
ar_value=['5','6','7','8']
def grow_dict():
    global dict
    for x in range(0,len(ar_key)):
        dict[ar_key[x]]=ar_value[x]

print'Available pairs: ',dict.items()
grow_dict()
print'Available pairs: ',dict.items()


