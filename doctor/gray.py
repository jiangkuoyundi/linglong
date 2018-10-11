# coding:utf-8

from bs4 import *
from urllib3 import *
import requests
from bs4 import *
import json
import urllib
import urlparse
import parse
# post请求登录
rs= requests.session()
payload = {'username': 'sunyuxin', 'password': 'rQAxtGafTiXkym'}
p = rs.post('http://navigator-admin.linglongtech.com/navigator_admin/login.do', data=payload)
graysn = ['SA03211182217992']
# 根据列表循环get请求获得数据
for grays in graysn:
    url = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=100&offset=0&start_date=2018-09-13+00:00:00&end_date=2018-09-13+23:59:59&SN='+str(grays)+'&_=1536756663096'
    r = rs.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    dic = soup.body.text
    dic = dic.replace('null','0')
    dic = dic.encode('UTF-8')
    dic = json.loads(dic)
    diclen = len(dic["rows"])
    print(dic["rows"][0]["sn"])
    print(dic["rows"][0]["id"])
    print(dic["rows"][0]["log_TYPE"])
    # 打印符合要求的数据，device_PLAY_INFO包含失败的字段
    for i in range(diclen):
        data = dic["rows"][i]["device_PLAY_INFO"]
        data = data.encode('UTF-8')
        if '失败' in data:
            print(dic["rows"][i]["sn"])
            print(dic["rows"][i]["log_TIME"])
            print(dic["rows"][i]["device_PLAY_INFO"])
            d = dic["rows"][i]["id"]
            d1= dic["rows"][i]["sn"]
            d2 = dic["rows"][i]["log_TIME"]
            d3 = dic["rows"][i]["device_PLAY_INFO"]
            print('   '+d1+':'+d2+d3)
            # 二次post请求，get请求中获得参数，再发送一次post请求
            event = {'uid':d , 'log_type': 2}
            p = rs.post('http://navigator-admin.linglongtech.com/navigator_admin/streamLogDetail', data=event)
            soup = BeautifulSoup(p.text, 'lxml')
            print(soup)

rs.close()

