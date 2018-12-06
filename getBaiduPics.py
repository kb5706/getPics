import requests
import re

#用输入的关键词拼接出搜索后的页面url
print('请输入搜索关键词')
keyword = str(input())
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&ct=201326592&v=flip'
pagecode = requests.get(url).text  #得到搜索页的源码
model =  re.compile('"objURL":"(.*?)",', re.S) #用正则表达式定义原图地址的规律
pic_url = re.findall('"objURL":"(.*?)",',pagecode,re.S)#匹配网页源代码中所有原图的地址

