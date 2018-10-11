# coding:utf-8
import subprocess
import time

# 循环查找音箱ID，查到再推出，否则隔3s查一次
# def checkVboxDevice():
#     while True:
#         time.sleep(3)
#         try:
#             ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#         except:
#             print('adb devices failed')
#         ps.wait()
#         data = ps.stdout.readlines()
#         data = ''.join(data)
#         if 'JYZ' not in data:
#                 # vboxid = vboxid.replace('device', '')
#                 # vboxid = vboxid.lstrip()
#                 # vboxid = vboxid.rstrip()
#             print('not found doctor device !')
#         else:
#             return True


def getVboxID():
    try:
        ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('adb devices failed')
    ps.wait()
    data = ps.stdout.readlines()
    # print(data)
    time.sleep(3)
    for vboxid in data:
        if 'JYZ' in vboxid:
            vboxid = vboxid.replace('device', '')
            vboxid = vboxid.lstrip()
            vboxid = vboxid.rstrip()
            return vboxid

print(getVboxID())


'''
# Get the speaker device ID, and return the device ID if the doctor device is detected, or False
def getVboxID():
    while True:
        try:
            ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            print('adb devices failed')
        ps.wait()
        data = ps.stdout.readlines()
        print(data)
        time.sleep(3)
        for vboxid in data:
            if 'JYZ' in vboxid:
                vboxid = vboxid.replace('device', '')
                vboxid = vboxid.lstrip()
                vboxid = vboxid.rstrip()
                return vboxid
'''


'''
# 获取音箱设备ID，加入到列表。如有设备返回一个列表(多个设备同时连接时使用)
def getVboxID():
    while True:
        time.sleep(3)
        try:
            ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            print('adb devices failed !')
        ps.wait()
        mylist=[]
        data = ps.stdout.readlines()
        print(data)
        for vboxid in data:
            if 'JYZ' in vboxid:
                vboxid = vboxid.replace('device', '')
                vboxid = vboxid.lstrip()
                vboxid = vboxid.rstrip()
                mylist.append(vboxid)
                return mylist
        break
    return mylist
'''
'''

def getPhoneID():
    ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    ps.wait()
    data = ps.stdout.readlines()
    for vboxid in data:
        if '6T7HNZPJDQHQUGFA' in vboxid:
            vboxid = vboxid.replace('device', '')
            vboxid = vboxid.lstrip()
            vboxid = vboxid.rstrip()
            return vboxid
'''


if __name__ == '__main__':
    print('pass')