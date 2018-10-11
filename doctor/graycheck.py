# coding:utf-8
from bs4 import *
from urllib3 import *
import requests
from bs4 import *
import json
import urllib
import urlparse
import parse

url = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=100&offset=0&start_date=2018-09-13+00%3A00%3A00&end_date=2018-09-13+23%3A59%3A59&SN=SA03211182943469&_=1536756663096'
# url2 = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=100&offset=0&start_date=2018-09-13+00:00:00&end_date=2018-09-13+23:59:59&SN=SA03211182943469&_=1536756663096'
# url进行切割
print(urlparse.urlsplit(url))
# url进行解析
print(urlparse.urlparse(url))
# url进行字符串解码
print(urlparse.unquote(url))
# url进行字符串编码
# print(urllib.quote(url))
# j = urllib.quote(url2)
# print(j)
# print(urlparse.unquote(j))

#
# rs= requests.session()
# payload = {'username': 'sunyuxin', 'password': 'rQAxtGafTiXkym'}
# p = rs.post('http://navigator-admin.linglongtech.com/navigator_admin/login.do', data=payload)
# graysn = ['SA03211182217992']
# for grays in graysn:
#     # url = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=10&offset=1&start_date=2018-09-13+00%3A00%3A00&end_date=2018-09-13+23%3A59%3A59&SN=SA03211182943469&_=1536808153979'
#     # url = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=100&offset=1&start_date=2018-09-13+00%3A00%3A00&end_date=2018-09-13+23%3A59%3A59&SN='+str(grays)+'&_=1536809716235'
#     url = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=100&offset=0&start_date=2018-09-13+00:00:00&end_date=2018-09-13+23:59:59&SN='+str(grays)+'&_=1536756663096'
#     # url = urllib.quote(url)
#     r = rs.get(url)
#
#     soup = BeautifulSoup(r.text,'lxml')
#     dic = soup.body.text
#     dic = dic.replace('null','0')
#     # print(dic)
#     # print(type(dic))
#     dic = dic.encode('UTF-8')
#     # print(dic)    # print(type(dic))
#     dic = json.loads(dic)
#     # print(dic)
#     # print(type(dic))
#     diclen = len(dic["rows"])
#     print(dic["rows"][0]["sn"])
#     print(dic["rows"][0]["id"])
#     print(dic["rows"][0]["log_TYPE"])
#     for i in range(diclen):
#         data = dic["rows"][i]["device_PLAY_INFO"]
#         data = data.encode('UTF-8')
#         if '失败' in data:
#             # print(dic["rows"][i]["sn"])
#             print(dic["rows"][i]["log_TIME"])
#             print(dic["rows"][i]["device_PLAY_INFO"])
#             d = dic["rows"][i]["id"]
#             d1= dic["rows"][i]["sn"]
#             d2 = dic["rows"][i]["log_TIME"]
#             d3 = dic["rows"][i]["device_PLAY_INFO"]
#             # print('   '+d1+':'+d2+d3)
#
#             event = {'uid':d , 'log_type': 2}
#             p = rs.post('http://navigator-admin.linglongtech.com/navigator_admin/streamLogDetail', data=event)
#             print(p)
#             #
#             # http = PoolManager()
#             # r = http.request('GET', 'http://navigator-admin.linglongtech.com/navigator_admin/streamLogDetail')
#             soup = BeautifulSoup(p.text, 'lxml')
#             print(soup)
#
# rs.close()

