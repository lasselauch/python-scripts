#www.lasselauch.com/lab/
#Use at your own risk
import os, re

def VersionUp(path='', only_last=False, increment='up'):
    if path is None:
        return

    if os.name == 'nt':
        pass

    pattern = '_(v|V)(\d+)'

    matches = re.findall(pattern, str(path))
    if only_last:
        matches = [matches.pop(-1)]

    oldpath = path

    #if not os.path.exists(oldpath):
        #oldpath = False

    for i, m in enumerate(matches):
        v, old = m
        padding = len(old)

        if increment == 'up':
            increment = int(old)+1
        if increment == 'down':
            increment = int(old)-1

        new = str(increment).zfill(padding)
        path = path.replace(old, new)

    #if not os.path.exists(path):
        #path = False

    return oldpath, path

myString = ".../tesatv01201/Folder_v112/Folder_v01212/TestGeo_V00121.abc"
myString = "/Volumes/Animation_CG/last_version/_V/scenes/scene_280/Maya/LOS_sc280/cache/alembic/LOS_sc280_sh090_Chuck_V12312.abc"
myString = r"D:\__WORK\ADIDAS\Adidas_Swim\30_C4d\RotatingVolleyball\RotatingVolleyball_v01.c4d"
myString = r"D:\Dropbox\180425_Adidas\25_AfxOut\SH01\SH01_PreComp_v03"
myString = r"D:\Dropbox\180425_Adidas\25_AfxOut\SH04\SH04_PreComp_v05\SH04_PreComp_v05_00000.dpx"
myString = r"D:\__WORK\UNFOLD\BMW_GKL\02_projects\3D\KRISTALL\Kristall_v09.c4d"
myString = r"D:\__WORK\ADIDAS\Adidas_Swim\30_C4d\lal\Bra_Setup\Bra_Setup_v02.c4d"

oldpath, newpath = VersionUp(path=myString, only_last=False, increment='up')

print oldpath
print newpath
