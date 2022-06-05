import os
f=[]
dr=[]
ph=[]
def ch_dr_list():
    os.chdir("C:\Users\kulbhushan.s\Desktop")
    for (dirpath, dirnames, filenames) in os.walk("C:\Users\kulbhushan.s\Desktop"):
        f.append(filenames)
        dr.append(dirnames)
        ph.append(dirpath)
        print filenames
    #print os.listdir("C:\Users\kulbhushan.s\Desktop")
ch_dr_list()
