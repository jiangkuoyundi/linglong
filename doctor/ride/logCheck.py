#-*- coding: utf-8 -*-
import subprocess
import time
import xlrd
def log(check):
    ads = 'adb shell tail -f /tmp/dingdong.log'
    # ads = 'ipconfig'
    mylist = []
    ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    star = time.time()
    while True:
        data = ps.stdout.readline()
        end = time.time()-star
        # print(data)
        # mylist.append(data)
        if check in data:
            break
        elif end>30:
            return -1
    return

if __name__ == '__main__':
    check = ''
    log(check)