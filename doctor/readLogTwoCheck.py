#-*- coding: utf-8 -*-
import subprocess
import time
import xlrd
import os
import sys
import killadbproc
import psutil
reload(sys)
sys.setdefaultencoding('utf-8')

# 获得subprocess启动的adb后台进程列表
def getadbproc():
    psl = []
    for proc in psutil.process_iter():
        if proc.name() == 'adb.exe':
            if proc.cmdline().count('tail')>0:
                psl.append(proc.pid)
                # print(psl)
    return psl
# 关闭subprocess启动的adb后台进程
def kill_adb():
    n = getadbproc()
    print(n)
    if len(n) > 2:
        mylenth = len(n)
        for ml in range(mylenth):
            os.system('taskkill -f /pid ' + str(n[ml]))
    else:
        print('adb process less 2')

def mylog(checkone,checktwo):
    ads = 'adb shell tail -f /tmp/dingdong.log'
    try:
        ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('stop in subprocess.Popen ')
    star = time.time()
    c = 0
    e = 0
    while True:
        data = ps.stdout.readline()
        end = time.time()-star
        result = True
        if checkone in data :
            print(data)
            c = 1
            if c + e > 1:
                ps.terminate()
                kill_adb()
                return result
        elif checktwo in data:
            print(data)
            e=1
            if c + e > 1:
                ps.terminate()
                kill_adb()
                return result
        elif end>60:
            result = False
            ps.terminate()
            kill_adb()
            return result

def checksong():
    # 单个运行
    # os.system(str(2) + '.wav')
    testresult = mylog('transContant = 我要听周杰伦的歌曲。', 'OnPlaySongChanged songName = 周杰伦')
    if testresult == True:
        print('==========================歌曲测试通过================================')
    elif testresult  == False:
        print('==========================歌曲超时失败================================')
    else:
        print('==========================歌曲测试失败================================')


checksong()