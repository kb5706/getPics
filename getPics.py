import urllib
import re
import requests
def getBaiduPage(baiduKeyword,page,n):   #拼接成百度搜索url的方法
    page=page*n
    baiduKeyword = urllib.parse.quote(baiduKeyword, safe='/')
    baiduUrl_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    baiduUrl = baiduUrl_begin + baiduKeyword + "&pn=" + str(page) + "&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0"
    return baiduUrl


def get_baidu_onepage_urls(onepageurl):     #这个方法看不太懂
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls

def down_baidu_pic(pic_urls):      #这个也有地方不明白
    """给出图片链接列表, 下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            string =str(i + 1) + '.jpg'
            with open(string, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue
