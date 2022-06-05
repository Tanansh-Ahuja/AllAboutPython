#python dictionaries

dict={'abcd':'1','efgh':'2','ijkl':'3'}

def dict_tst():
    global dict
    dict['hello']='4'
    
print "original Dictionary: ",dict
dict_tst()
print"Dictionary after alteration: ",dict
