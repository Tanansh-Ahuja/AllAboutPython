#delete from list

ar_d=['Hi','Hello','a','b','c']

def del_frm_list():
    global ar_d
    indx=int(raw_input('Enter a number b/w 1&5: '))-1
    print "Deleting '",ar_d[indx],"' from array"
    del ar_d[indx]

print 'Array before deletion',ar_d
del_frm_list()
print 'Array after deletion',ar_d
