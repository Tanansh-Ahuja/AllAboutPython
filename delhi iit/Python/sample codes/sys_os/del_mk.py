import os
import sys
import time

def del_fld():
    os.rmdir("C:\Users\kulbhushan.s\Desktop\\fld_1\\fld_2\\fld_3")
    time.sleep(5)
    os.mkdir("C:\Users\kulbhushan.s\\Desktop\\fld_1\\fld_2\\fld_3")
del_fld()
