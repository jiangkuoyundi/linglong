#coding:utf-8
import chardet
import time
import os

'''
项目：doctor音箱
目的：破坏性测试，删除config文件，验证系统重启后是否自动生成被删除的文件；
状态：已完成；
时间：2018/4/27
作者：李盈辉
'''


'''
查看文件目录
'''
def adbshell():
    adbshell = 'adb shell ls'
    doscomm = os.popen(adbshell).readlines()

    for doss in doscomm:
        print doss.decode("gb2312")

'''
重启系统
'''

def reboot():
    adbshellr = 'adb shell reboot'
    os.popen(adbshellr)
'''
删除文件
'''
def rmfiles(filepath,filename):
    adbshell = 'adb shell rm '
    os.popen(adbshell+filepath+filename)

'''
查看文件目录
'''
def ls(filepath):
    adbshell = 'adb shell ls '
    confiles = os.popen(adbshell+filepath).readlines()
    for filen in confiles:
        #print filen.decode("gb2312")
        return filen
    return

'''
打开文件
'''
def getlog():
    fo = open("../files/cfgfile.txt", "r")
    print"文件名为: ", fo.name
    lines = fo.readlines()
    return lines
    # 关闭文件
    fo.close()

if __name__ == "__main__":

    ss = getlog()
    i=1
    while i<len(ss):
        i += 2
        filepath = ss[i-3].rstrip('\n')
        filename = ss[i-2].rstrip('\n')
        # 返回结果是字符串，判断方法type(),对返回结果进行判断是否存在指定文件，如果文件存在则删除；
        lsfile = ls(filepath)
        if lsfile.find(filename)!=-1:
            print 'find the file :'+filename
            rmfiles(filepath,filename)
            time.sleep(3)
            reboot()
            time.sleep(120)
        else:
            print 'could not find the file :'+filename

        #等待重启后查看配置文件是否存在,如果存在说明程序自动重启后生成了，则通过

        if lsfile.find(filename)!=-1:
            print 'success！！',filename

