#-*- coding: utf-8 -*-
import subprocess
import locale
import codecs
import time
import xlrd
import os
import sys
import psutil
reload(sys)
sys.setdefaultencoding('utf-8')

# 获得pid列表
def getadbpid():
    psl = []
    for proc in psutil.process_iter():
        if proc.name() == 'adb.exe':
            # print(proc.pid)
            # proc.cpu_times
            psl.append(proc.pid)
    return psl


# 获得占用cpu的adb pid
def getnonzeropid():
    for proc in psutil.process_iter():
        if proc.name() == 'adb.exe':
            if proc.cpu_percent(interval=3) != 0.0:
                print(proc.pid)
            return proc.pid

def kill_adb():
    n = getadbpid()
    s = getnonzeropid()
    print(n)
    print(s)
    if len(n) > 2 and s == 1:
        n.remove(s)
        print(n)
    else:
        print('adb process No need to close ')

    mylenth = len(n)
    print(mylenth)

    if mylenth == 0:
        print('only zero  adb.exe ')
    elif mylenth == 1:
        print('only one adb.exe')
    elif mylenth == 2:
        print('only two adb.exe')
    elif mylenth > 2:
        mylenth = mylenth - 1
        for pid in range(mylenth):
            print(n[pid])
            os.system('taskkill -F /PID ' + str(n[pid]))

def readLogTwoCheck(check,expect):
    ads = 'adb shell tail -f /tmp/dingdong.log'
    # ads = 'ipconfig'
    mylist = []
    ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    star = time.time()
    c = 0
    e = 0
    while True:
        data = ps.stdout.readline()
        end = time.time()-star
        result = True
        # print(data)
        # mylist.append(data)
        if check in data :
            print(data)
            c = 1
            f = c + e
            if f >1:
                return result
        elif expect in data:
            print(data)
            e=1
            f = c + e
            if f>1:
                return result
        elif end>60:
            result = False
            return result
