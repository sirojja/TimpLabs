#!/usr/bin/python3 

import hashlib
import sys
import os

def check_passwd(tpass):
    passwd=open("/root/templates.tbl").readline().rstrip()
    hashp = hashlib.md5(tpass.encode('utf-8')).hexdigest()
    if (passwd == hashp):
        return 1
    else:
        return 0


def help():
    print("This program prohibits copying, renaming and creating files with forbidden names. The file with forbidden names is located in /root/templates.tbl and is readable only by root. To run the program, you need to authenticate with a password, only root knows it.")
    print("Usage: sudo ./deny.py [OPPTIONS]")
    print("-h      -> Manual of this propramm")
    print("--start -> Start programm")
    print("--stop  -> Stop programm")



def deny():
    tpass = str(input("Password:"))
    if (check_passwd(tpass) == 1):
        print("Now you cannot copy, delete and create to files with forbidden names.")
        os.system(./deny.sh &)
    else:
        print("Wrong password")


def access():
    tpass = str(input("Password:"))
    if (check_passwd(tpass) == 1):
        os.system("./kill.sh")
        print("Program was stopped")
    else:
        print("Wrong password")



if name == "main":
    if len (sys.argv) > 1:
        option = sys.argv[1]
        if (option == "-h"):
            help()
        if (option == "--start"):
            deny()
        if (option == "--stop"):
            access()
    else:
        print ("Oh, you need only one option. See -h")
#text = str(input())
