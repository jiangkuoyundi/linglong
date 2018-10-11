#-*- coding: utf-8 -*-
import requests
import re
import time
import hashlib
import base64
import struct
import xlrd
import readExcel

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
#讯飞开放平台注册申请应用的应用ID(appid)
APPID = "5afd1b4d"
API_KEY = "bd9c4abcbba2f0dc71810141911c1010"

''' 
语音合成接口将文字信息转化为声音信息，同时提供了众多极具特色的发音人（音库）供您选择。
'''


def getHeader():
    curTime = str(int(time.time()))
    param = "{\"aue\":\"" + AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
    paramBase64 = base64.b64encode(param)
    m2 = hashlib.md5()
    m2.update(API_KEY + curTime + paramBase64)
    checkSum = m2.hexdigest()
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'X-Real-Ip': '106.38.113.2',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def getBody(text):
        data = {'text':text}
        return data

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()

'''
定义函数读取表格的用例内容
'''
def getExcleData(i):
    try:
        data = xlrd.open_workbook('doctorAutoCase.xlsx')
    except :
        print('open excel feiled !')

    #shrang = range(data.nsheets)
    sh = data.sheet_by_name("Sheet3")
    #获取Excel表格里的数据，i表示行，j表示列。行和列都是从0开始计数。
    cell_value = sh.cell_value(i,4)
    return cell_value


'''
通过调用表格返回的数据进行文字到语音的转换。其中range(40)表示读取表格前40行的用例，根据函数定义，也可以改为读取所有有内容的行数
'''
if __name__ == '__main__':
    for i in range(1,118):
        r = requests.post(URL,headers=getHeader(),data={'text':getExcleData(i)})
        print(str(i)+getExcleData(i))
        contentType = r.headers['Content-Type']
        if contentType == "audio/mpeg":
            sid = r.headers['sid']
            if AUE == "raw":
                writeFile("audioA/"+str(i)+".wav", r.content)
            else :
                writeFile("audioA/"+str(i)+".mp3", r.content)
            print "success "
        else :
            print r.text
