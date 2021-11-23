
import hashlib
import os
import datetime
import sys
import time

key = "secretkey" #key to hash
filename = "reg.txt" #hiden file with times
flag = "/usr/secret/flag.txt" #register flag
filename_t = "time.txt"

def changefile(n):
    file = open(filename, "w")
    time = str(os.path.getmtime(filename))
    #print(time)
    tmp = str(n) + key + time
    dec_checksum = tmp.encode('utf-8')
    h = hashlib.sha256(dec_checksum)
    enc_checksum = h.hexdigest()
    #print(tmp)
    ans = str(n) + " " + enc_checksum
    file.write(ans)
    file.close()
    #print(os.path.getmtime(filename))
    #print(enc_checksum)
def changefile_t(n):
    file = open(filename_t, "w")
    time = str(os.path.getmtime(filename_t))
    #print(time)
    tmp = str(n) + key + time
    dec_checksum = tmp.encode('utf-8')
    h = hashlib.sha256(dec_checksum)
    enc_checksum = h.hexdigest()
    #print(tmp)
    ans = str(n) + " " + enc_checksum
    file.write(ans)
    file.close()
    #print(os.path.getmtime(filename))
    #print(enc_checksum)

def check_license():

    fline=open(filename).readline().rstrip()
    data = fline.split()
    tmp = str(data[0]) + key + str(os.path.getmtime(filename))
    dec_checksum = tmp.encode('utf-8')
    h = hashlib.sha256(dec_checksum)
    enc_checksum = h.hexdigest()
    #print(dec_checksum)
    #print(enc_checksum)
    #print(data)
    if(enc_checksum == data[1]):
        #print("Ok")
        return 1
    else:
        #print("Not Ok")
        return 0

def check_license_t():

    fline=open(filename_t).readline().rstrip()
    data = fline.split()
    tmp = str(data[0]) + key + str(os.path.getmtime(filename_t))
    dec_checksum = tmp.encode('utf-8')
    h = hashlib.sha256(dec_checksum)
    enc_checksum = h.hexdigest()
    #print(dec_checksum)
    #print(enc_checksum)
    #print(data)
    if(enc_checksum == data[1]):
        #print("Ok")
        return 1
    else:
        #print("Not Ok")
        return 0

def check_flag(path_to_flag):
    if (os.path.exists(path_to_flag)):
        #print("Ok")
        return 1
    else:
        #print("Not Ok")
        return 0

def get_time(n):
    start_time = time.time()
    ans = 0
    s = str(input("What is your name? "))
    ans = n - (time.time() - start_time)
    changefile_t(ans)
    if (ans > 0):
        return s
    else:
        return "-1"

def program_tl():
    fline=open(filename_t).readline().rstrip()
    data = fline.split()
    n = float(data[0])
    if (n > 0 and check_license_t()):
        fio = get_time(n)
        if (fio == "-1"):
            #print("((((")
            a = 1
        else:
            print ("Welcome to the club,", fio)
            f = open('test.txt')
            text = f.read()
            f.close()
            c = text.count(fio)
            if (c == 0):
                file = open("test.txt", "a")
                file.write(fio)
                file.close()
            else:
                print("You already registered!")
    fline=open(filename_t).readline().rstrip()
    data = fline.split()
    n = float(data[0])
    if (n > 0):
        print("Do you like my program? How many seconds you can use it for free? I'm sorry but only", n)
    else:
        print("What do you think about buying the full version of my perfect program?)")
    

def program_sl():
    fline=open(filename).readline().rstrip()
    data = fline.split()
    n = int(data[0])
    if(check_license() and check_flag(flag) and n > 0):
        #print("I can work", n)
        fio = str(input("What is your name? "))
        f = open('test.txt')
        text = f.read()
        f.close()
        c = text.count(fio)
        if (c == 0):
          file = open("test.txt", "a")
          file.write(fio)
          file.close()
          print ("Welocome to the club,", fio)
        else:
            print("You already registered!")
        changefile(n - 1)
        if (n > 1):
            print("Do you like my program? How many times you can use it for free? I'm sorry but only", n - 1)
        else:
            print("What do you think about buying the full version of my perfect program?)")
    else:
        print("What do you think about buying the full version of my perfect program?)")

def check_files():
    if(os.path.exists(flag) and os.path.exists(filename) and os.path.exists(filename)):
        return 1
    else:
        return 0

def help():
    print("Hey! Here is a free version of my perfect program. It knows how to do incredible things. For example, it might ask your name and write your lovely name to a file.")
    print("Unfortunately, you may not use my program all the time. You have 5 trial runs of the program as well as one minute of use. Make good use of this time.")
    print("Do not delete any program files. My beautiful program won't work without them. And also I forbid trying to hack my program. If you try to hack, you will have to buy the full version.")
    print("Usage:")
    print("--sl - Start-limited")
    print("--tl - Time-limited")
    print("  -h - help")
#changefile_t(60.0)
#changefile(5)

#res = check_license()
#print(res)
#print(os.path.getmtime("reg.txt"))
#a = check_flag(flag)
#print(a)
if __name__ == "__main__":
    if len (sys.argv) > 1:
        if (check_files()):
            cmd = sys.argv[1]
            if (cmd == "--tl"):
                program_tl()
            elif (cmd == "--sl"):
                program_sl()
            elif (cmd == "-h"):
                help()
            else:
                print ("Use -h to see some help")
        else:
            print("Something seems to have gone wrong. Contact the developers")
    else:
        print ("Use -h to see some help")