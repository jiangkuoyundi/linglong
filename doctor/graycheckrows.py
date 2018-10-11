# coding:utf-8

import requests
from bs4 import *
from time import strftime,localtime
import json
import xlrd

def getExcleData(i):
    try:
        data = xlrd.open_workbook('graysn.xlsx')
    #    print data
    except Exception,e:
        print str(e)
    #shrang = range(data.nsheets)
    sh = data.sheet_by_name("Sheet1")
    #获取Excel表格里的数据，i表示行，j表示列。行和列都是从0开始计数。
    cell_value = sh.cell_value(i,0)
    return cell_value

def writelog(str):
    # 每天生成一个日志文件
    logname = strftime("%Y-%m-%d", localtime())
    logpath = 'C:\\a\doctor\\'+logname+'garysn.txt'
    fo = open(logpath, 'a')
    fo.write(str )
    fo.write('\n')
    fo.close()

'''
爬取的内容是Unicode编码，先转换为string字符串才能转换为字典。
从字典中读取内容，还是Unicode编码，可以直接拼接。但是作为string类型的参数传递给函数是，必须再次转换成string
'''
if __name__ == '__main__':
    s= requests.session()
    payload = {'username': 'sunyuxin', 'password': 'rQAxtGafTiXkym'}
    p = s.post('http://navigator-admin.linglongtech.com/navigator_admin/login.do', data=payload)
    # graysn = ['SA03211182217992']
    # for grays in graysn:
    for row in  range(1,4000):
        url = 'http://navigator-admin.linglongtech.com/navigator_admin/streamLog?limit=100&offset=1&start_date=2018-09-13+18%3A26%3A00&end_date=2018-09-13+23%3A59%3A59&SN='+str(getExcleData(row))+'&_=1536809716235'
        r = s.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        dic = soup.body.text
        dic = dic.replace('null','0')
        # print(dic)
        # print(type(dic))
        dic = dic.encode('UTF-8')
        # print(dic)    # print(type(dic))
        dic = json.loads(dic)
        # print(dic)
        # print(type(dic))
        try:
            diclen = len(dic["rows"])
        except:
            print('diclen = len(dic["rows"])')
        if diclen > 0:
            print(dic["rows"][0]["sn"])
            writelog(dic["rows"][0]["sn"])
            # print(dic["rows"][0]["id"])
            # print(dic["rows"][0]["log_TYPE"])
            for i in range(diclen):
                data = dic["rows"][i]["device_PLAY_INFO"]
                data = data.encode('UTF-8')
                if '失败' in data:
                    # print(dic["rows"][i]["sn"])
                    # print(dic["rows"][i]["log_TIME"])
                    # print(dic["rows"][i]["device_PLAY_INFO"])
                    d = dic["rows"][i]["id"]
                    d1 = dic["rows"][i]["sn"]
                    d2 = dic["rows"][i]["log_TIME"]
                    d3 = dic["rows"][i]["device_PLAY_INFO"]
                    print(type(d3))
                    d1 = d1.encode('UTF-8')
                    d2 = d2.encode('UTF-8')
                    d3 = d3.encode('UTF-8')
                    print(type(d3))
                    d4 = '   ' + d1 + ';' + d2 +  ';' +d3
                    print('   ' + d1 + ';' + d2 +  ';' +d3)
                    writelog(d4)

    s.close()

