import datetime
import requests
import os
import re

begin = datetime.date(2014,7,1)
end = datetime.date(2020,5,1)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    a = d.strftime("%Y-%m-%d")
    d += delta
    url = "https://static-event.benghuai.com/new_mihoyo_homepage/images/download/cg/origin/"+a+".jpg"
    #print (url)
    r = requests.get(url)
    #print (str(r))
    if (str(r) == "<Response [200]>"):

        urls = re.findall('http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                      url)
        print(urls)

        if not os.path.exists('bh2'):

            os.mkdir('bh2')

#保存图片
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

        for url in urls:

            file_name = url.split('/')[-1]

            r = requests.get(url,headers=headers)

            with open('bh2' + '/' +file_name,'wb') as f:

                f.write(r.content)