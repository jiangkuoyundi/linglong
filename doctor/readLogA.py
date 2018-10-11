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

def mylog(check,expect):
    ads = 'adb shell tail -f tmp/dingdong.log'
    ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    star = time.time()
    c = 0
    e = 0
    while True:
    # for i in range(100):
        data = ps.stdout.readline()
        # data = ps.stdout.read()
        end = time.time()-star
        result = True
        print(data)
        if check in data :
            print(data)
            c = 1
            f = c + e
            if f >1:
                ps.terminate()
                kill_adb()
                return result
        elif expect in data:
            print(data)
            e=1
            f = c + e
            if f>1:
                ps.terminate()
                kill_adb()
                return result
        elif end>60:
            result = False
            ps.terminate()
            kill_adb()
            return result

#定义函数读取表格的用例内容
def getExcleData(i):
    try:
        data = xlrd.open_workbook('doctorAutoCase.xlsx')
    #    print data
    except Exception,e:
        print str(e)
    #shrang = range(data.nsheets)
    sh = data.sheet_by_name("Sheet1")
    #获取Excel表格里的数据，i表示行，j表示列。行和列都是从0开始计数。
    cell_value = sh.cell_value(i,3)
    return cell_value

def runD(i):
    os.system(str(i) + '.wav')
    check = getExcleData(i)
    mylog(check)

if __name__ == '__main__':
    # 单个运行
    transcontent = '我要听周杰伦的青花瓷'
    music_is_playable = 'PlayerController OnPlay songName = 青花瓷'
    testresult = mylog(transcontent, music_is_playable)
    print(testresult)
    if testresult == True:
        print('==========================测试通过================================')
    elif testresult  == False:
        print('==========================超时失败================================')
    else:
        print('==========================测试失败================================')


# 批量运行
    '''
    for i in range(1,10):
        time.sleep(2)
        os.system(str(i)+'.wav')
        ch = getExcleData(i)
        print('检查点'+str(ch))
        if mylog(ch) == 0:
            print('==========================测试通过================================')
        else:
            print('==========================测试失败================================')
'''