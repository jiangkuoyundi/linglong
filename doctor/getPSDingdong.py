# coding:utf-8
import serial,time,subprocess
# 获取叮咚进程
def getPSDingdong(deviceID):
    psdingdong = 'adb -s '+str(deviceID)+' shell ps'
    dingdong = True
    try:
        ps = subprocess.Popen(psdingdong, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        thread_dingdong = ps.stdout.readlines()
    except:
        print('The speaker device was not detected')
    thread_dingdong = ''.join(thread_dingdong)
    print(thread_dingdong)
    # if 'dingdong' in thread_dingdong and 'btservice' in thread_dingdong and 'appmainprog' in thread_dingdong:
    if 'dingdong'  and 'btservice'  and 'appmainprog' in thread_dingdong:
        return dingdong
    else:
        dingdong = False
        return dingdong
    return 0

dingdong = getPSDingdong('JYZ28843')
if dingdong == True:
    print('音箱正常')
elif dingdong == False:
    print('音箱崩溃')
else:
    print('正常结束')