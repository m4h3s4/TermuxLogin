#!/bin/python

import os,sys,time
x = "lukman"
y = "kill"

def bersih():
    os.system("clear")

def menu():
    bersih()
    print "+-------------------------------+"
    print "Author : Trey.Killer-Anonymous"
    print "Youtube : Noel Qeen"
    print "Facebook :Trey.Killer"
    print "Instagram : lx_m3n96"
    print "Github : https://github.com/Trey.Killer"
    print "+-------------------------------+"
    print "Menu"
    print "[1] Install CRACK"
    print "[2] Install FB-Cracker"
    print "[3] Install fbtarget"
    print "[4] Install Hackfb"
    print "[5] Install MBFv2"
    print "[6] Install igtools"
    print "[7] Install Report3"
    print "[0] Exit/Keluar"
    pil = raw_input("Masukan Nomor ~> ")
    if pil =="1":
       os.system("python2 Crack.py")
    elif pil =="2":
       os.system("pkg update && pkg upgrade -y")
    elif pil =="3":
       os.system("pkg update && pkg upgrade -y")
    elif pil =="4":
         print "File Belum Tersedia"
    elif pil =="5":
         print "File Belum Tersedia"
    elif pil =="6":
         print "File Belum Tersedia"
    elif pil =="7":
         print "File Belum Tersedia"
    elif pil =="0":
        sys.exit()

menu()
