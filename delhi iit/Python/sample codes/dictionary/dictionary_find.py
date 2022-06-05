#search Dictionary Elements

dict={'a':'1','b':'2','c':'3','d':'4'}

def find_dict():
    global dict
    if dict.has_key(raw_input("Tye in the index to search: ")):
        print "Yes we have it"
    else:
        print "No we don't have it"

print'Available keys: ',dict.keys()
find_dict()
print'Available pairs: ',dict.items()

