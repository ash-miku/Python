import requests

from lxml import etree

import re

import os

#获取网页
num =0
for i in range(1,6):
    num = num + 1
    url="https://www.bh3.com/content/bh3Cn/getContentList?pageSize=9&pageNum="+str(num)+"&channelId=177"
    r = requests.get(url)
    newurl = r.text.replace('\\','')
    # 解析网页

    urls = re.findall('http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                      newurl)
    # print(urls)
    # print(newurl)
    if not os.path.exists('bh3'):

        os.mkdir('bh3')

#保存图片
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    for url in urls:

        file_name = url.split('/')[-1]

        r = requests.get(url,headers=headers)

        with open('bh3' + '/' +file_name,'wb') as f:

            f.write(r.content)

