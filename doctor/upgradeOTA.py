# coding:utf-8
import serial,time,subprocess
import os
import clickApplication
import sendMailnonatta


#继电器第7位开十六进制
write_open_7=[0x01,0x06,0x00,0x06,0x00,0xFF,0x29,0x8B,0x01,0x01,0x00,0x00,0x00,0x10,0x3D,0xC6]

#继电器第7位关十六进制
write_close_7 = [0x01,0x06,0x00,0x06,0x00,0x00,0x69,0xCB,0x01,0x01,0x00,0x00,0x00,0x10,0x3D,0xC6]

#继电器第8位开十六进制
write_open_8=[0X01,0X06,0X00,0X07,0X00,0XFF,0X78,0X4B,0X01,0X01,0X00,0X00,0X00,0X10,0X3D,0XC6]

#继电器第8位关十六进制
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
    ser = serial.Serial("com1", 9600, 8, 'E', 1, 0)
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

# Get the speaker device ID, and return the device ID if the doctor device is detected, or False
def getVboxID():
    ps = subprocess.Popen('adb devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    ps.wait()
    data = ps.stdout.readlines()
    for vboxid in data:
        if 'JYZ' in vboxid:
            vboxid = vboxid.replace('device', '')
            vboxid = vboxid.lstrip()
            vboxid = vboxid.rstrip()
            return vboxid
    return False

# 获取手机设备ID，
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
    # 每个版本导入相应的配置文件信息。
    appconfigjson = 'adb -s ' + str(deviceID) + ' push C:\APullLog\Doctor\pushSN\\appconfig.json data/dingdong/etc/'
    async = 'adb -s ' + str(deviceID) + ' shell sync'
    areboot = 'adb -s ' + str(deviceID) + ' shell reboot'

    for s in [touch,nvram_helper,chmod,psn,appconfigjson,async,areboot]:
        print(s)
        try:
            ps = subprocess.Popen(s, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            pass
        time.sleep(2)
        # ps.wait()
        print(ps.stdout.readlines())

if __name__ == '__main__':

    print('-----environment monitoring-----')
    if getPhoneID() == False:
        print('No mobile devices detected')
        exit()
    if check_com_port() == False:
        print('No port detected')
        exit()
    if getVboxID()==False:
        print('No sound box detected')
        exit()
    #获取烧录前音箱设备ID
    deviceID = getVboxID()
    print('--获取烧录前音箱设备ID和设备版本--')
    print(deviceID)
    print(getVersion(deviceID))
    # 定义已上线的音箱版本
    # onVer = [225,205,188,161,151,133,129,120,114,112,104,101,97,79]
    # onVer = [188]
    onVer = [120,114,112,104,101,97,79]

    for onlineVer in onVer:
        startime = time.time()

        ser=serial.Serial("com1",9600,8,'E',1,0)
        sw = ser.write(write_open_7)

        time.sleep(3)
        #安装固件
        openCMD(onlineVer)
        time.sleep(3)
        #关闭电源
        ser.write(write_close_7)
        time.sleep(3)
        #按下音量加键
        ser.write(write_open_8)
        time.sleep(5)
        # 打开电源
        ser.write(write_open_7)
        time.sleep(5)
        # 松开音量加键
        ser.write(write_close_8)

        # 等待烧录完成,获取音箱ID
        time.sleep(60)
        print('--根据音箱ID烧录SN，导入配置文件--')
        deviceID = getVboxID()
        time.sleep(3)
        #导入SN并重启
        pushSN(deviceID)
        time.sleep(120)
        print('--获取烧录SN后重启的，设备ID和音箱版本--')
        deviceID = getVboxID()
        time.sleep(15)
        oldversion = getVersion(deviceID)
        print(deviceID)
        print(getVersion(deviceID))
        #关闭端口
        ser.close()
        time.sleep(25)
        '''注释1 检查升级前的bet文件
        # ddjet = 'adb -s ' + str(deviceID) + ' pull data/dingdong/vbox/ivw/dingdong.jet C:\APullLog\Doctor\\betold'
        ps = subprocess.Popen(ddjet, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ps.wait()
        print(ps.stdout.readlines())
        print(os.path.getsize('C:\APullLog\Doctor\\betold\dingdong.jet'))
        oldDingdongjet = os.path.getsize('C:\APullLog\Doctor\\betold\dingdong.jet')
        '''

        # 启动 appium
        openAppium()
        time.sleep(10)
        ''' 增加一个点击APP的操作'''
        try:
            clickApplication.appP()
        except:
            print('app operation failure')
        time.sleep(150)
        '''kill cmd.exe'''
        os.system("start taskkill /IM cmd.exe")

        '''获取音箱升级后的设备ID'''
        print('--获取升级重启后，设备ID和音箱版本--')
        deviceID = getVboxID()
        print('--现在最新的版本--' + getVersion(deviceID))

        #对比一下是不是预期的版本，如果不是则继续等待再检查一次
        for i in range(3):
            if getVersion(deviceID)!= '1.0.0.255':
                print('音箱升级失败，等待一分钟再检测一次最新版本，连续三次后退出')
                time.sleep(60)
                print('--继续等待后的最新版本--' + getVersion(deviceID))
            else:
                print('--音箱升级成功--')
                break

        newversion = getVersion(deviceID)
        ''' 注释1 导出升级后版本的文件
        ddjet = 'adb -s ' + str(deviceID) + ' pull data/dingdong/vbox/ivw/dingdong.jet C:\APullLog\Doctor\\betnew'
        ps = subprocess.Popen(ddjet, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ps.wait()
        print(ps.stdout.readlines())
        print(os.path.getsize('C:\APullLog\Doctor\\betnew\dingdong.jet'))
        newDingdongjet = os.path.getsize('C:\APullLog\Doctor\\betnew\dingdong.jet')
        
        if oldDingdongjet == newDingdongjet:
            print('--dingdong.jet文件大小一致，说明升级有问题--')
        else:
            print('--dingdong.jet文件大小不一致，说明升级正常--')
        '''
        # time.sleep(180)
        useTime = time.time() - startime
        s = '邮件内容 ' \
            '<br> 1，升级前版本 %s ；' \
            '<br> 2，升级后版本 %s ；' \
            '<br> 3，升级用时间 %s ；' \
            '<br> ' % (oldversion,newversion,str(useTime) )
        sendMailnonatta.sendMail(s)
