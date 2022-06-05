#add data to list

list_d=['hello','there']
def add_to_list():
    global list_d
    list_d.append('added')

print "Array before addition: ",list_d
add_to_list()
print "Array after addition: ",list_d
