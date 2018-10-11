# coding:utf-8
import psutil
import os


# 获得pid列表
# def getadbpid():
#     psl = []
#     for proc in psutil.process_iter():
#         if proc.name() == 'adb.exe':
#             # print(proc.pid)
#             # proc.cpu_times
#             psl.append(proc.pid)
#     return psl


# 获得主进程adb pid
# def getnonzeropid():
#     for proc in psutil.process_iter():
#         if proc.name() == 'adb.exe':
#             # print(proc.cmdline())
#             if proc.cmdline().count('server') > 0:
#                 print(proc.pid)
#                 return proc.pid

# 获得subprocess启动的adb后台进程列表
def getadbproc():
    psl = []
    for proc in psutil.process_iter():
        if proc.name() == 'adb.exe':
            if proc.cmdline().count('tail')>0:
                psl.append(proc.pid)
                print(psl)
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

if __name__ == '__main__':
    kill_adb()