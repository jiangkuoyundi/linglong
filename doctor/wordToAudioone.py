#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64

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


if __name__ == '__main__':
    r = requests.post(URL,headers=getHeader(),data={'text':"捞仔捞仔，我要听周杰伦的青花瓷"})
    # print(r)
    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        if AUE == "raw":
            writeFile("audioA/"+"288.wav", r.content)
        else :
            writeFile("audioA/"+"288.mp3", r.content)
        print "success "
    else :
        print r.text
