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
def mylog(check):
    ads = 'adb shell tail -f /tmp/dingdong.log'
    # ads = 'ipconfig'
    mylist = []
    ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    star = time.time()
    while True:
        data = ps.stdout.readline()
        end = time.time()-star
        print(data)
        # mylist.append(data)
        if check in data:
            print('==========================测试通过================================')
            break
        elif end>30:
            print('==========================测试失败================================')
            return -1
    return
#定义函数读取表格的用例内容
def getExcleData(i):
    try:
        data = xlrd.open_workbook('C:\\Python27\\Lib\\site-packages\\MyLibrary\\doctorAutoCase.xlsx')

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
    i=1
    runD(i)
    '''
    控制台运行脚本
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
