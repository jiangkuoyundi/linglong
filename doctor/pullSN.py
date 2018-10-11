# coding:utf-8

import serial,time,subprocess
import os

# 导入配置文件，功能等同于烧录SN
def pushSN(deviceName):
    # 给音箱导入SN等信息，相当于自动联网
    touch = 'adb -s ' + str(deviceName) + ' shell touch /data/dingdong/etc/log.txt'
    nvram_helper = 'adb -s ' + str(deviceName) + ' push C:\APullLog\Doctor\pushSN\\nvram_helper.bin /tmp'
    chmod = 'adb -s ' + str(deviceName) + ' shell chmod 777 tmp/nvram_helper.bin'
    psn = 'adb -s ' + str(
        deviceName) + ' shell /tmp/nvram_helper.bin  -w SA03111180100301,b0:f1:ec:66:67:4a,b0:f1:ec:66:67:49,c83b304d-b823-463e-99c4-21af644b12b5,6769e6d5-e29a-43a1-9305-9548f68f322a3f22d236-b755-4a33-ac6a-48f0b00b817d'
    # 每个版本导入相应的配置文件信息。
    appconfigjson = 'adb -s ' + str(deviceName) + ' push C:\APullLog\Doctor\pushSN\\appconfig.json data/dingdong/etc/'
    async = 'adb -s ' + str(deviceName) + ' shell sync'
    areboot = 'adb -s ' + str(deviceName) + ' shell reboot'

    for s in [touch,nvram_helper,chmod,psn,appconfigjson,async,areboot]:
        print(s)
        try:
            ps = subprocess.Popen(s, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        except:
            pass
        time.sleep(2)
        ps.wait()
        print(ps.stdout.readlines())

if __name__ == '__main__':
    pushSN('JYZ13338')