import os
import win32api
from time import sleep

gsdrive = "C"
hsrdrive = "C"

drives = win32api.GetLogicalDriveStrings()
if len(drives) != 1:
    gsdrive = input("Enter the drive you install Genshin Impact: ")
    hsrdrive = input("Enter the drive you install Honkai: Star Rail: ")
    

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
path = os.path.abspath("init.py")
path = path.replace("init.py", "main")
os.mkdir(path)

batpath = os.path.join(path, "getloc.bat")
f = open(batpath, "x")
genshinpath = os.path.join(path, "gsloc.txt")
hsrpath = os.path.join(path, "hsrloc.txt")
f.write("@echo off" + "\nchdir /d " + gsdrive + ':\ ' + "\ndir /s /b genshinimpact.exe > " + genshinpath + "\nchdir /d " + hsrdrive + ":\ " + "\ndir /s /b starrail.exe > " + hsrpath)
f.close()
os.system(batpath)

desktop = os.path.join(desktop, "Hoyoverse")
os.mkdir(desktop)

gsbatpath = os.path.join(desktop, "Genshin Impact.bat")
f = open(genshinpath, "r")
w = open(gsbatpath, "x")
genshinpath = f.readline()
w.write("@echo off" + "\n" + gsdrive + ":" + '\n"' + genshinpath)
f.close()
w.close()

hsrbatpath = os.path.join(desktop, "Star Rail.bat")
f = open(hsrpath, "r")
w = open(hsrbatpath, "x")
hsrpath = f.readline()
f.close()
w.write("@echo off" + "\n" + hsrdrive + ":" + '\n"' + hsrpath)
w.close()

os.remove(os.path.join(path, "getloc.bat"))
os.remove(os.path.join(path, "gsloc.txt"))
os.remove(os.path.join(path, "hsrloc.txt"))
os.rmdir(path)

gsbatpath = '"' + gsbatpath + '"'
hsrbatpath = '"' + hsrbatpath + '"'
temp = input("Run Genshin Impact/Honkai: Star Rail now?\n0.No\n1.Genshin Impact\n2.Honkai: Star Rail\n3.Both\n")
match temp:
    case "0":
        exit()
    case "1":
        os.system(gsbatpath)
    case "2":
        os.system(hsrbatpath)
    case "3":
        os.system(gsbatpath)
        os.system(hsrbatpath)



