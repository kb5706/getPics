import requests
import re
import os

#用输入的关键词拼接出搜索后的页面url
print('请输入搜索关键词')
keyword = str(input())
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&ct=201326592&v=flip'
pagecode = requests.get(url).text  #得到搜索页的源码
model =  re.compile('"objURL":"(.*?)",', re.S) #用正则表达式定义原图地址的规律
pic_url = re.findall('"objURL":"(.*?)",',pagecode,re.S)#匹配网页源代码中所有原图的地址
i = 1
path = 'D:\\Cloud\\' + keyword + '\\'

isExists=os.path.exists(path)
if not isExists:
    # 如果不存在则创建目录
    # 创建目录操作函数
    os.makedirs(path)

    print(path + ' 创建成功')
    isExists = True
else:
    # 如果目录存在则不创建，并提示目录已存在
    print(path + ' 目录已存在')
    isExists = False


for each in pic_url:    #把所有网页源代码里的图片遍历
    print(each)
    try:
        pic = requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:         #抛掉网络无法连接的图片错误
        print('【Error】此图片无法下载')
        continue
    location = 'D:\\Cloud\\' + keyword + '\\' + keyword + '_' + str(i) + '.jpg'     #定义图片存储位置
    picObject = open(location, 'wb')                                #打开图片对象，新建 or 重写图片
    picObject.write(pic.content)                                    #写入图片内容
    picObject.close()                                               #关闭图片对象
    i += 1                                                          #计数器加1