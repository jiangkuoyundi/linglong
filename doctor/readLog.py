#-*- coding: utf-8 -*-
import subprocess
import locale
import codecs
import time
import xlrd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
功能描述：
1，读取检查点；
2，播放语搜音频文件；
3，通过分析dingdong.log进行检查点匹配；如果日志中包含检查点则认为测试通过，否则测试失败，最长检索30秒，可自定义；
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
            ps.terminate()
            return 1
        elif end > 180:
            ps.terminate()
            return 2
        else:
            time.sleep(10)
    return

# 带着检查点逐行分析dingdong.log，如果检查到预期结果则返回0，否则返回-1
def mylog(check):
    ads = 'adb shell tail -f /tmp/dingdong.log'
    ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    star = time.time()
    check = check.lstrip()
    check = ''.rstrip()
    result = True
    while True:
        data = ps.stdout.readline()
        end = time.time()-star
        # print(data)
        # mylist.append(data)
        if check in data:
            ps.terminate()
            return result
        elif end > 30:
            result = False
            ps.terminate()
            return result

#读取表格sheet1下的检查点，第三列的行，返回检查点。
def getExcleData(i):
    try:
        data = xlrd.open_workbook('doctorAutoCase.xlsx')
    except Exception,e:
        print('no find')

    try:
        sh = data.sheet_by_name("Sheet1")
    except NameError,e:
        print('no find Sheet1')

    #获取Excel表格里的数据，i表示行，j表示列。行和列都是从0开始计数。
    cell_value = sh.cell_value(i,3)
    return cell_value

# 播放语搜音频文件
def runD(i):
    os.system(str(i) + '.wav')
    check = getExcleData(i)
    mylog(check)

if __name__ == '__main__':
    # 检查设备是否已连接，如果已连接则继续，否则退出。
    if check_devices()==1:
        print('find devices')
    else:
        exit()

    # 控制台批量运行脚本，自定义读取行数。range(1,10)表示读取1-9行。
    for i in range(1,10):
        time.sleep(2)
        os.system('audio\\'+str(i)+'.wav')
        ch = getExcleData(i)
        ch = ''.join(ch)
        ch = ch.rstrip()
        ch = ch.lstrip()
        print(str(i)+'检查点:'+str(ch))
        if mylog(ch) == 0:
            print(str(i)+'==============测试通过======================')
        # elif mylog(ch) == -1:
        else:
            print(str(i)+'==============测试失败======================')

