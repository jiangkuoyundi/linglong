# coding:utf-8
import time

t = time.strftime("%H", time.localtime())
print(type(t))

t = float(t)
print(t)
t1 = int(t)
print(t1)

if t1<23:
    print('ttt')
