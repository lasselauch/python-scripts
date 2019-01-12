#www.lasselauch.com/lab/
#Use at your own risk
import os
import shutil
from datetime import datetime

#thispath = os.path.dirname(os.path.abspath(__file__))
search_dir = r'D:\_TUTORIALS\_RECORDINGS'

os.chdir(search_dir)
files = filter(os.path.isfile, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] # add path to each file
#files.sort(key=lambda x: os.path.getmtime(x))

tfolders = []

for fn in files:
    #Skip *.bat Launch-File
    launcher = os.path.basename(fn)
    if launcher == 'sort_folder.bat':
        continue

    fntime = os.path.getmtime(fn)
    tstamp = datetime.fromtimestamp(fntime).strftime('%y%m%d')
    #Create Unique Folder by Date
    if tstamp not in tfolders:
        tfolders.append(tstamp)

    #Create Folders if not already created
    dst = os.path.join(search_dir, tstamp)
    if not os.path.exists(dst):
        os.mkdir(dst)

    #Move Files in dedicated Folders
    for folder in tfolders:
        if tstamp == folder:
            try:
                shutil.move(fn, dst)
            except shutil.Error as e:
                print e, " ... move to 'duplicates' folder..."
                duplicates = os.path.join(search_dir, 'duplicates')
                if not os.path.exists(duplicates):
                    os.mkdir(duplicates)
                shutil.move(fn, duplicates)
