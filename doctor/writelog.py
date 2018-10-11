# coding:utf-8

import os ,sys
from time import strftime,ctime,localtime

def writelog(str):
    # 每天生成一个日志文件
    logname = strftime("%Y-%m-%d", localtime())
    logpath = 'C:\\a\doctor\\'+logname+'.txt'
    fo = open(logpath, 'a')
    fo.write(str )
    fo.write('\n')
    fo.close()

writelog('{}开始歌曲点播测试。。'.format(ctime()))




# # 打开文件
# fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
#
# # 写入字符串
# os.write(fd, "This is test")
#
# # 关闭文件
# os.close( fd )
#
# print "关闭文件成功!!"