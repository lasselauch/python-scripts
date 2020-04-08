import os
import shutil
from datetime import datetime

path = '/Users/lasse/Desktop'

for fn in os.listdir(path):
    source = os.path.join(path, fn)
    
    mtime = os.path.getmtime(source)
    date_folder = datetime.fromtimestamp(mtime).strftime('%Y/%m')

    destination = os.path.join(path, date_folder)
    if not os.path.exists(destination):
        os.makedirs(destination)

    shutil.move(source, destination)
