# coding:utf-8
#爬取bug列表
import requests
import json
from bs4 import *
from requests.auth import HTTPBasicAuth
from time import sleep
from urlparse import urlparse,urlsplit
# s=requests.Session()

headers = {
    "Accept": 'application/json, text/plain, */*',
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Authorization":"Basic YWRtaW46cFZVbVl3aUpqSmVlOXBaWg==",
    "Content-Length": "802",
    "content-type": 'application/x-ldjson',
    "Host": 'elk.linglongtech.com',
    "kbn-version": "5.1.1",
    "Origin": 'http://elk.linglongtech.com',
    "Proxy-Connection": 'keep-alive',
    "Referer": "http://elk.linglongtech.com/app/kibana",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


payload = {"index":["logstash-ms-service-context-2018.09.17"],"ignore_unavailable":"true","preference":"1537262816502","size":"200","sort":[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}],"query":{"bool":{"must":[{"query_string":{"query":"\"SA03211183058493\" AND \"update.do\"","analyze_wildcard":"true"}},{"range":{"@timestamp":{"gte":"1537200000000","lte":"1537286399999","format":"epoch_millis"}}}],"must_not":[]}},"highlight":{"pre_tags":["@kibana-highlighted-field@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{}},"require_field_match":"false","fragment_size":"2147483647"},"_source":{"excludes":[]},"aggs":{"2":{"date_histogram":{"field":"@timestamp","interval":"30m","time_zone":"Asia/Shanghai","min_doc_count":"1"}}},"stored_fields":["*"],"script_fields":{},"docvalue_fields":["@timestamp"]}

auth = HTTPBasicAuth('admin','pVUmYwiJjJee9pZZ')

r = requests.post(url='http://elk.linglongtech.com/elasticsearch/_msearch',data=json.dumps(payload),headers = headers,auth=auth)

soup = BeautifulSoup(r.text,'lxml')

print(r)
print(soup)


# print(r.status_code)
# print(r.headers)
# print(r.cookies)
# print(r.history)