# coding:utf-8


import subprocess
#获取音箱版本号，对字符串进行解析后获得
ps = subprocess.Popen('adb shell dingdong -v', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
appjson = ps.stdout.readlines()
appjson = appjson[-1].split(':')
print(appjson[1])
appjson = appjson[1].rstrip()
appjson = appjson.lstrip()
print(appjson)
print(appjson[1])
print(type(appjson[1]))


