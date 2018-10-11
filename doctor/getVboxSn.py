#!/usr/bin/python
# coding:utf-8
import sys
import os
import subprocess
import time
import sendMailnonatta

'''检查doctor设备是否已经连接,连续检查三分钟，如果超时则返回2，如果检测到设备则返回1'''
def check_devices():
    star = time.time()
    while True:
        ads = 'adb devices'
        try:
            ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            pass
        data = ps.stdout.readlines()
        data = ''.join(data)
        print(data)
        end = time.time() - star
        if 'JYZ' in data:
            return 1
        elif end > 180:
            return 2
        else:
            time.sleep(10)
    return

# 获取音箱设备ID，加入到列表。如有设备返回一个列表
def getVboxID():
    ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    ps.wait()
    mylist=[]
    data = ps.stdout.readlines()
    for vboxid in data:
        if 'JYZ' in vboxid:
            vboxid = vboxid.replace('device', '')
            vboxid = vboxid.lstrip()
            vboxid = vboxid.rstrip()
            mylist.append(vboxid)
            # print(mylist)
    return mylist

# 获取音箱设备的sn,根据不同的设备ID进入设备，返回设备的SN.
def getSN(ID):
    c = 'adb -s '+str(ID)+' shell dingdong -s'
    try:
        time.sleep(1)
        ps = subprocess.Popen(c, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        pass
    star = time.time()
    while True:
        data = ps.stdout.readline()
        end = time.time() - star
        # print(data)
        # mylist.append(data)
        if 'SN:' in data:
            data = data.split(':')
            print(data[2])
            return data[2]
        elif end > 60:
            return -1
    return 1
# 导出SN
def pullDd(id,sn):
    path = 'C:\\A\\Doctor\\'+str(sn)
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
        print(path)
    else:
        print('path is exists')
    ads = 'adb -s '+str(id)+' pull /tmp/dingdong.log  C:\A\Doctor\\'+str(sn)+'\\'
    try:
        ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('devices no found')
    ps.wait()
    data = ps.stdout.readlines()
    print(data)
# 分析SN
def analyzeDd(sn):
    # 打开文件
    path='C:\A\Doctor\\'+str(sn)+'\dingdong.log'
    try:
        fo = open(path, "r")
    except:
        print('未找到文件')
    print"--文件名为: ", fo.name

    lines = fo.readlines()
    # content = 'LYB'
    # 循环读取文件，发现关键词则进行处理。-1表示失败，说明没找到。
    i = 0
    for line in lines:
        # if line.find(content) != -1 or line.find('INTO')!= -1:
        if 'angle' in line:
            # if line.find('CAEProcessor')!= -1:
            print line
            i += 1
    # print('--发现关键词angle的次数：'+str(i)+str(sn))
    # 关闭文件
    fo.close()
    return (i)

'''运行播放器播放音频文件'''
def playVideo(name):

    os.system(name)
    # time.sleep(2)

if __name__ == '__main__':
    # 一个音源
    rouseA = 'shunping.mp3'

    # 定义播放循环次数
    num = 3

    if check_devices()==1:
        print('adb devices pass')
    else:
        print('adb devices fail')
        exit()

    for i in range(num):
        time.sleep(2)
        playVideo(rouseA)
        time.sleep(2)



    for id in getVboxID():
        print(id)
        time.sleep(3)

        sn = getSN(id)
        print(sn)
        time.sleep(3)

        pullDd(id,sn)

        time.sleep(3)
        rse = float(analyzeDd(sn))
        print(rse)

        if num == rse:
            print(str(sn)+'-----唤醒次数等于播放次数--------')
            print('--本次唤醒率:{:.2%}'.format(rse / float(num)))
        elif num > rse:
            print(str(sn)+'-----唤醒次数小于播放次数--------')
            print('--本次唤醒率:{:.2%}'.format(rse / float(num)))
        else:
            print(str(sn)+'-----唤醒次数大于播放次数--------')
            print('--本次唤醒率:{:.2%}'.format(rse / float(num)))

        s='测试结束(音箱sn): '+str(sn) + \
          '<br>唤醒次数:'+str(rse)+ \
          '<br>播放次数:'+str(num)+\
          '<br>唤醒率:{:.2%}'.format(rse / float(num))

        sendMailnonatta.sendMail(s)