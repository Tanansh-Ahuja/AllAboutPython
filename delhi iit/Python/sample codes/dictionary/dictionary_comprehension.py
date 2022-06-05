#Add Dictionary Elements

dict={'zero':'0'}
ar_key=['a','b','c','d','e','f','g','h']
ar_value=['1','2','3','4','5','6','7','8']

def grow_dict():
    global dict
    dict={ar_key[x]:ar_value[x] for x in range(0,len(ar_key))}
    

print'Available pairs: ',dict.items()
grow_dict()
print'Available pairs: ',dict.items()


