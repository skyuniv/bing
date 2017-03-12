import requests
# 下载模块.
import urllib.request
import time

url = 'http://cn.bing.com/'
image_0  = requests.get(url).content
image_1 = image_0.decode('utf-8','ignore')
image_2 = image_1.split("hprichbg/rb/")[1].split("_1920x1080.jpg")[0]#split函数的运用切割特定字符
image_url = "http://cn.bing.com/az/hprichbg/rb/"+image_2+"_1920x1080.jpg"
image_name = time.strftime("%Y-%m-%d", time.localtime())
print(image_name)
image_save = urllib.request.urlretrieve(image_url, 'H:\\bing_image\\%s.jpg' % image_name)
print("Image is ok")
