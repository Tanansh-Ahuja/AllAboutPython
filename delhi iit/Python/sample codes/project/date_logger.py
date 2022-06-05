from datetime import datetime

with open("d:\log.text",'ab') as a:
    a.write( str(datetime.now()).split('.')[0]+'\n')
    a.close()
