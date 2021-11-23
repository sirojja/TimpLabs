import os

filename = "reg.txt" #hiden file with times
flag = "/usr/secret/flag.txt" #register flag
filename_t = "time.txt"

if(os.path.exists(flag):
    print("The program has already been installed")
else:
    os.system("touch /usr/secret/flag.txt")

