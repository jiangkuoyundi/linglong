# coding:utf-8
import serial,time,subprocess
import os
from time import sleep,ctime,strftime,localtime
import clickApplication
import sendMailnonatta
import upgradeotacheck

# 继电器第7位开十六进制
write_open_7=[0x01,0x06,0x00,0x06,0x00,0xFF,0x29,0x8B,0x01,0x01,0x00,0x00,0x00,0x10,0x3D,0xC6]
# 继电器第7位关十六进制
write_close_7 = [0x01,0x06,0x00,0x06,0x00,0x00,0x69,0xCB,0x01,0x01,0x00,0x00,0x00,0x10,0x3D,0xC6]
# 继电器第8位开十六进制
write_open_8=[0X01,0X06,0X00,0X07,0X00,0XFF,0X78,0X4B,0X01,0X01,0X00,0X00,0X00,0X10,0X3D,0XC6]
# 继电器第8位关十六进制
write_close_8 = [0X01,0X06,0X00,0X07,0X00,0X00,0X38,0X0B,0X01,0X01,0X00,0X00,0X00,0X10,0X3D,0XC6]

def openCMD(onlineVer):
    try:
        os.system('start C:\Users\\admin\PycharmProjects\linglong\dingdong\doctor\\accomplish\\bat\\'+str(onlineVer)+'.bat')
    except:
        print('--The Vbox version number does not exist--')

def openAppium():
    try:
        os.system('start C:\Users\\admin\PycharmProjects\linglong\dingdong\doctor\\accomplish\\bat\startAppium.bat')
    except:
        print('--appium boot failed--')
# Check whether the serial port is open
def check_com_port():
    ser = serial.Serial("com2", 9600, 8, 'E', 1, 0)
    if ser.is_open==True:
        ser.close()
        return True
    return False

# Check the version of the speaker after the speaker is restarted
def getVersion(deviceID):

    ver = 'adb -s '+str(deviceID)+' shell dingdong -v'
    try:
        ps = subprocess.Popen(ver, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        appjson = ps.stdout.readlines()
        appjson = appjson[-1].split(':')
        appjson = appjson[1].rstrip()
        appjson = appjson.lstrip()
    except:
        print('The speaker device was not detected')
    # print(appjson[1])
    return appjson

# Continuously check the speaker device and return True if detected. Check every 3 seconds.
def checkVboxDevice():
    for i in range(60):
        sleep(3)
        try:
            ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            print('adb devices failed')
        ps.wait()
        data = ps.stdout.readlines()
        data = ''.join(data)
        if 'JYZ' in data:
            return True
        else:
            print('no found box device !')

# Get the speaker device ID, and return the device ID if the doctor device is detected, or False
def getVboxID():
    try:
        ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('adb devices failed')
    ps.wait()
    data = ps.stdout.readlines()
    print(data)
    for vboxid in data:
        if 'JYZ' in vboxid:
            vboxid = vboxid.replace('device', '')
            vboxid = vboxid.lstrip()
            vboxid = vboxid.rstrip()
            print(vboxid)
            return vboxid
    return False

# Get the phone device ID，
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
    return False

# Import configuration file, function is equivalent to burning SN
def pushSN(deviceID):
    # Import SN and other information to the speaker, which is equivalent to automatic networking
    touch = 'adb -s ' + str(deviceID) + ' shell touch /data/dingdong/etc/log.txt'
    nvram_helper = 'adb -s ' + str(deviceID) + ' push C:\APullLog\Doctor\pushSN\\nvram_helper.bin /tmp'
    chmod = 'adb -s ' + str(deviceID) + ' shell chmod 777 tmp/nvram_helper.bin'
    psn = 'adb -s ' + str(
        deviceID) + ' shell /tmp/nvram_helper.bin  -w SA03111180100301,b0:f1:ec:66:67:4a,b0:f1:ec:66:67:49,c83b304d-b823-463e-99c4-21af644b12b5,6769e6d5-e29a-43a1-9305-9548f68f322a3f22d236-b755-4a33-ac6a-48f0b00b817d'
    appconfigjson = 'adb -s ' + str(deviceID) + ' push C:\APullLog\Doctor\pushSN\\appconfig.json data/dingdong/etc/'
    async = 'adb -s ' + str(deviceID) + ' shell sync'
    areboot = 'adb -s ' + str(deviceID) + ' shell reboot'

    for s in [touch,nvram_helper,chmod,psn,appconfigjson,async,areboot]:
        print(s)
        try:
            ps = subprocess.Popen(s, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            pass
        sleep(1)
        print(ps.stdout.readlines())

# Get the ding dong process
def getPSDingdong(deviceID):
    psdingdong = 'adb -s '+str(deviceID)+' shell ps'
    dingdong = True
    try:
        ps = subprocess.Popen(psdingdong, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('The speaker device was not detected')

    thread_dingdong = ps.stdout.readlines()
    thread_dingdong = ''.join(thread_dingdong)

    print('开始打印dingdong进程。。')
    print(thread_dingdong)
    print('结束打印dingdong进程。。')

    if 'dingdong' and 'btservice' and 'appmainprog' in thread_dingdong:
        return dingdong
    else:
        dingdong = False
        return dingdong

def readlog(check,deviceid):
    ads = 'adb -s '+str(deviceid)+' shell tail -f /tmp/dingdong.log'
    ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    star = time.time()
    # check = check.lstrip()
    # check = ''.rstrip()
    while True:
        data = ps.stdout.readline()
        end = time.time()-star
        # print(data)
        # mylist.append(data)
        if check in data:
            check = True
            return check
        elif end > 30:
            check = False
            return check
    return 0


# 导出log
def pulllog(deviceid,onlineVer):
    path = 'c:\\a\\doctor\\'+str(onlineVer)
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        print('path is exists')

    ads = 'adb -s '+str(deviceid)+' pull /tmp/dingdong.log  C:\\a\doctor\\'+str(onlineVer)+'\\'
    try:
        ps = subprocess.Popen(ads, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    except:
        print('devices no found')
    ps.wait()
    data = ps.stdout.readlines()
    print(data)
def writelog(str):
    # 每天生成一个日志文件
    logname = strftime("%Y-%m-%d", localtime())
    logpath = 'C:\\a\doctor\\'+logname+'.txt'
    fo = open(logpath, 'a')
    fo.write(str )
    fo.write('\n')
    fo.close()

if __name__ == '__main__':

    print('{}-----environment monitoring-----'.format(ctime()))
    if getPhoneID() == False:
        print('{}--No mobile devices detected'.format(ctime()))
        writelog('{}--No mobile devices detected'.format(ctime()))
        exit()
    else:
        print('{}--find mobile'.format(ctime()))
        writelog('{}--find mobile'.format(ctime()))
    if check_com_port() == False:
        print('{}--No port detected'.format(ctime()))
        writelog('{}--No port detected'.format(ctime()))
        exit()
    else:
        print('{}--find port'.format(ctime()))
        writelog('{}--find port'.format(ctime()))
    if getVboxID()==False:
        print('No box detected'.format(ctime()))
        writelog('No box detected'.format(ctime()))
        exit()
    else:
        print('find box')
        writelog('find box')
    # 获取烧录前音箱设备ID
    deviceID_1 = getVboxID()
    VBoxVersion_1 = getVersion(deviceID_1)
    print('{}--获取烧录前音箱设备ID和设备版本--'.format(ctime()))
    writelog('{}--获取烧录前音箱设备ID和设备版本--'.format(ctime()))
    print(deviceID_1)
    writelog(deviceID_1)
    print(VBoxVersion_1)
    writelog(VBoxVersion_1)
    # 定义已上线的音箱版本    NLINEVERSION = [292,271,255,225,205,188,161,151,133,129,120,114,112,104,101,97,79]
    ONLINEVERSION = [255,133]
    # onVer = [188]
    EXPECTVERSION = '1.0.1.348'
    print('本次升级到的新版本：'+EXPECTVERSION)
    writelog('本次升级到的新版本：'+EXPECTVERSION)
    for onlineVer in ONLINEVERSION:
        startime = time.time()

        ser=serial.Serial("com2",9600,8,'E',1,0)
        sw = ser.write(write_open_7)

        sleep(3)
        print('{}开始烧录固件。。'.format(ctime()))
        writelog('{}开始烧录固件。。'.format(ctime()))
        # 安装固件
        openCMD(onlineVer)

        sleep(3)
        # 关闭电源
        ser.write(write_close_7)
        sleep(3)
        # 按下音量加键
        ser.write(write_open_8)
        sleep(5)
        # 打开电源
        ser.write(write_open_7)
        sleep(5)
        # 松开音量加键
        ser.write(write_close_8)

        # 等待烧录完成,获取音箱ID
        sleep(30)
        print('{}结束烧录固件。。'.format(ctime()))
        writelog('{}结束烧录固件。。'.format(ctime()))
        # 检查一下doctor音箱是否已经存在
        for i in range(6):
            gtb = getVboxID()
            gtb = str(gtb)
            if 'JYZ' in gtb:
                break
            else:
                sleep(5)
                print('No box detected')
        # deviceID_2烧录固件后的音箱id
        deviceID_2 = getVboxID()
        sleep(6)

        print('{}开始导入配置文件。。'.format(ctime()))
        writelog('{}开始导入配置文件。。'.format(ctime()))
        # 导入SN并重启
        pushSN(deviceID_2)
        print('{}结束导入配置文件。。'.format(ctime()))
        writelog('{}结束导入配置文件。。'.format(ctime()))

        # 关闭电源
        ser.write(write_close_7)
        sleep(6)
        # 打开电源
        ser.write(write_open_7)
        # 关闭端口
        ser.close()

        print('{}导入配置文件后设备ID和音箱版本--'.format(ctime()))
        writelog('{}导入配置文件后设备ID和音箱版本--'.format(ctime()))
        # deviceID_3 导入配置文件后设备ID
        if checkVboxDevice()==True:
            deviceID_3 = getVboxID()
            sleep(10)
            oldversion = getVersion(deviceID_3)
            print(deviceID_3)
            print(oldversion)

        ''' 增加一个点击APP的操作'''
        if onlineVer < 105:
            # Start the appium
            openAppium()
            sleep(5)
            try:
                clickApplication.appP()
            except:
                print('app operation failure')
        else:
            print('{}此版本音箱会自动升级，不用借助APP--'.format(ctime()))
            writelog('{}此版本音箱会自动升级，不用借助APP--'.format(ctime()))

        # 检查音箱是否升级后重启
        for i in range(60):
            if checkVboxDevice()==True:
                deviceID_4 = getVboxID()
                if deviceID_4 == deviceID_3:
                    sleep(5)
                    print(deviceID_4,deviceID_3)
                else:
                    print(deviceID_4,deviceID_3)
                    break

        '''kill cmd.exe'''
        os.system("start taskkill /IM cmd.exe")

        '''获取音箱升级后的设备ID'''
        deviceID_5 = getVboxID()
        VBoxVersion_2 = getVersion(deviceID_5)
        print('{}--获取升级重启后，设备ID和音箱版本--'.format(ctime()))
        writelog('{}--获取升级重启后，设备ID和音箱版本--'.format(ctime()))
        print('--现在最新的版本--' + VBoxVersion_2)
        writelog('--现在最新的版本--' + VBoxVersion_2)

        # 对比一下是不是预期的版本
        if getVersion(deviceID_5) == EXPECTVERSION:
            print('{}与预期版本一致，音箱升级成功--'.format(ctime()))
            writelog('{}与预期版本一致，音箱升级成功--'.format(ctime()))
        else:
            print('{}与预期版本不一致，音箱升级失败--'.format(ctime()))
            writelog('{}与预期版本不一致，音箱升级失败--'.format(ctime()))

        print('{}开始歌曲点播测试。。'.format(ctime()))
        writelog('{}开始歌曲点播测试。。'.format(ctime()))
        # 升级后检查歌曲点播
        sleep(10)
        print('{}开始歌曲点播测试。。'.format(ctime()))
        writelog('{}开始歌曲点播测试。。'.format(ctime()))

        os.system('C:\Users\\admin\PycharmProjects\linglong\dingdong\doctor\\accomplish\\audioA\\' + str(288) + '.wav')
        checkone = 'transContant = 我要听周杰伦的青花瓷。'
        checktwo = 'PlayerController OnPlay singerName = 周杰伦'
        testresult = upgradeotacheck.mylog(checkone, checktwo, deviceID_5)
        if testresult==True:
            print('{}歌曲测试通过。'.format(ctime()))
            writelog('{}歌曲测试通过。'.format(ctime()))
        else:
            print('{}歌曲测试失败。'.format(ctime()))
            writelog('{}歌曲测试失败。'.format(ctime()))

        print('{}结束歌曲点播测试。。'.format(ctime()))
        writelog('{}结束歌曲点播测试。。'.format(ctime()))
        sleep(5)
        useTime = time.time() - startime
        newversion = getVersion(deviceID_5)
        getdingdong = getPSDingdong(deviceID_5)
        if getdingdong == True:
            print('音箱升级后dingdong没有崩溃。')
            writelog('音箱升级后dingdong没有崩溃。')
            print('开始导出日志。')
            pulllog(deviceID_5,onlineVer)
            print('结束导出日志。')
            s = '邮件内容 ' \
                '<br> 1，升级前版本 %s ；' \
                '<br> 2，升级后版本 %s ；' \
                '<br> 3，升级后dingdong进程正常 ；' \
                '<br> 4，升级用时间 %s 秒；' \
                '<br> ' % (oldversion, newversion, str(useTime))
            sendMailnonatta.sendMail(s)
        elif getdingdong == False:
            print('音箱升级后dingdong崩溃！')
            writelog('音箱升级后dingdong崩溃！')
            print('{}开始导出日志。'.format(ctime()))
            pulllog(deviceID_5)
            print('{}结束导出日志。'.format(ctime()))
            s = '邮件内容 ' \
                '<br> 1，升级前版本 %s ；' \
                '<br> 2，升级后版本 %s ；' \
                '<br> 3，升级后dingdong进程崩溃！ ；' \
                '<br> 4，升级用时间 %s 秒；' \
                '<br> ' % (oldversion, newversion, str(useTime))
            sendMailnonatta.sendMail(s)
        sleep(30)
