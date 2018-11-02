import re

def VersionUp(path="", last_version=False):
    if path == "":
        return
    pattern = '_(v|V)(\d+)'
    matches = re.findall(pattern, path)
    if last_version:
        matches = [matches.pop(-1)]

    oldpath = path

    for i, m in enumerate(matches):
        v, old = m
        padding = len(old)
        new = str(int(old)+1).zfill(padding)
        path = path.replace(old, new)

    return oldpath, path

#myString = ".../tesatv01201/Folder_v112/Folder_v01212/TestGeo_V00121.abc"
#myString = "/Volumes/Animation_CG/last_version/_V/scenes/scene_280/Maya/LOS_sc280/cache/alembic/LOS_sc280_sh090_Chuck_V12312.abc"
#myString = "D:\Dropbox\180425_Adidas\25_AfxOut\SH01\SH01_PreComp_v03"
#myString = "D:\__WORK\ADIDAS\Adidas_Swim\30_C4d\RotatingVolleyball\RotatingVolleyball_v01.c4d"
#myString = "D:\Dropbox\180425_Adidas\25_AfxOut\SH04\SH04_PreComp_v05\SH04_PreComp_v05_00000.dpx"
myString = "D:\__WORK\UNFOLD\BMW_GKL\02_projects\3D\KRISTALL\Kristall_v08.c4d"

oldpath, newpath = VersionUp(myString, False)

print oldpath
print newpath
