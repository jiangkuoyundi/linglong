#!/usr/bin/python
# coding:utf-8
import sys
import os
import subprocess
import time
'''
项目：doctor项目；
目的：分析log日志，提取需要的信息；（可以单条件和复合条件查询）
状态：已完成；
时间：2018/8/6
作者：李盈辉
'''

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

'''运行播放器播放音频文件'''
def playVideo(name):

    os.system(name)
    # time.sleep(2)

'''检查dingdong.log是否存在，如果存在返回1，否则返回0'''
def check_dingdong_log():
    ads = 'adb shell ls tmp '
    try:
        ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('未检测到设备')
    ps.wait()
    for i in range(2):
        data = ps.stdout.readline()
        print(data)
        if 'dingdong' in data:
            return 1
    return 0

'''导出dingdong.log文件，用于分析唤醒关键词'''
def pullDd():
    ads = 'adb pull /tmp/dingdong.log  C:\APullLog\Doctor'
    adsA = 'adb pull /tmp/dingdong.log  C:\APullLog\Doctor'
    try:
        ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('未检测到设备')
    ps.wait()
    data = ps.stdout.readlines()
    print(data)

'''删除dingdong.log文件，避免原来的日志干扰分析结果'''
def rmDd():
    ads = 'adb shell rm /tmp/dingdong.log'
    try:
        ps = subprocess.Popen(ads,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    except:
        print('未检测到设备')

    subprocess.Popen('adb shell reboot', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

'''创建dingdong.log文件'''

def mkDd():
    ads = 'adb shell touch /data/dingdong/etc/log.txt'
    try:
        ps = subprocess.Popen(ads,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    except:
        print('未检测到设备')
    ps.wait()
    data = ps.stdout.readlines()
    print(data)
    subprocess.Popen('adb shell reboot', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)


'''分析dingdong.log文件，返回唤醒关键词出现的次数'''
def analyzeDd():
    # 打开文件
    try:
        fo = open("C:\APullLog\Doctor\dingdong.log", "r")
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
    print('--发现关键词angle的次数：'+str(i))
    # 关闭文件
    fo.close()
    return (i)

if __name__ == '__main__':
    #定义播放音频文件
    rouse = ['tts.mp3','keyang.mp3','shunping.mp3']
    # 一个音源
    rouseA = 'shunping.mp3'

    # 定义播放循环次数
    num = 3

    #初次运行环境检查。检查设备是否连接，如果没有连接设备直接退出运行。
    if check_devices()==1:
        print('adb devices pass')
    else:
        print('adb devices fail')
        exit()

    #初次运行环境检查。检查是否存在dingdong.log，没有则创建，已有则删除
    if check_dingdong_log()==1:
        rmDd()
    else:
        mkDd()
    # 等待音箱重启
    time.sleep(10)
    if check_devices()==1:
        print('find devices')



    for i in range(num):
        time.sleep(2)
        playVideo(rouseA)
        time.sleep(2)

    # 播放完毕后导出dingdong.log，并进行分析
    time.sleep(5)
    # 导出目录：C:\APullLog\Doctor
    pullDd()
    # 计算音箱唤醒率,计算公式：音箱被唤醒总次数/唤醒词播放总次数
    ana = analyzeDd()
    rse = float(ana)
    if num == rse:
        print('-----唤醒次数等于播放次数--------')
        print('--本次唤醒率:{:.2%}'.format(rse / float(num)))
    elif num > rse:
        print('-----唤醒次数小于播放次数--------')
        print('--本次唤醒率:{:.2%}'.format(rse / float(num)))
    else:
        print('-----唤醒次数大于播放次数--------')

    # 删除dingdong.log,并重启音箱
    time.sleep(5)
    rmDd()

    # 先等音箱关闭，然后等待音箱重启
    time.sleep(10)
    if check_devices() == 1:
        print('find devices')











'''
    # 循环运行播放tts，循环一次，分析一次唤醒次数，并打印出唤醒率
    for name in rouse:
        for i in range(num):
            time.sleep(2)
            playVideo(name)
            time.sleep(2)

        # 播放完毕后导出dingdong.log，并进行分析
        time.sleep(5)
        # 导出目录：C:\APullLog\Doctor
        pullDd()
        # 计算音箱唤醒率,计算公式：音箱被唤醒总次数/唤醒词播放总次数
        ana = analyzeDd()
        rse = float(ana)
        if num == rse:
            print('-----唤醒次数等于播放次数--------')
            print('--本次唤醒率:{:.2%}'.format(rse / float(num)))
        elif num > rse:
            print('-----唤醒次数小于播放次数--------')
            print('--本次唤醒率:{:.2%}'.format(rse / float(num)))
        else:
            print('-----唤醒次数大于播放次数--------')

        #删除dingdong.log,并重启音箱
        time.sleep(5)
        rmDd()

        # 先等音箱关闭，然后等待音箱重启
        time.sleep(10)
        if check_devices() == 1:
            print('find devices')
'''

