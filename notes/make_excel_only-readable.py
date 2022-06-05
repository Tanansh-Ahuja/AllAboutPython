import os
from stat import S_IREAD, S_IRGRP, S_IROTH
os.chmod('C:\\Users\\com\\Desktop\\a.xlsx', S_IREAD|S_IRGRP|S_IROTH)
