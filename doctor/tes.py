# coding:utf-8
from subprocess import Popen,PIPE
import sys
# 通过adb实时读取log文件
p1=Popen('adb shell tail -f /tmp/dingdong.log',stdin=PIPE,stdout=PIPE,shell=False)

for i in range(10):
    # 当log不打印为空时，下面无返回值，停止执行。
    output = p1.stdout.readline()
    print(output)

p1.terminate()
    # s = sys.stdout.write('sss')
    # print(s)

