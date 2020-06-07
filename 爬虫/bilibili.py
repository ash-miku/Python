import requests
import re
import os
import time

#获取网页
uid = input("请输入B站用户uid:")
print("uid is :",uid)
page_num = input("请输入想要爬取相簿页数:")
print("Total page num is :",page_num)
print()
print("Start-----------------------------------")
print()

start = time.time()

num = 0
file_success_num = 0
file_failed_num = 0

for i in range(0,int(page_num)):
    url="https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid="+str(uid)+"&page_num="+str(num)+"&page_size=30&biz=all"
    num = num + 1
    r = requests.get(url)
    newurl = r.text.replace('\\','')
    # 解析网页

    urls = re.findall('http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                      newurl)
    #print(urls)

    #print(newurl)
    if not os.path.exists('bilibili/'+str(uid)):

        os.makedirs('bilibili/'+str(uid))

#保存图片
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    for url in urls:

        file_name = url.split('/')[-1]

        r = requests.get(url,headers=headers)

        if (str(r) == "<Response [200]>"):

            with open('bilibili/'+str(uid) + '/' +file_name,'wb') as f:

                f.write(r.content)

            file_success_num += 1

            print("正在下载:",file_name)

        else :
            print("正在下载: ---------------404 NOT FOUND----------------")
            file_failed_num += 1

end = time.time() - start

filePath = "bilibili/"+str(uid)

def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            #print(f)
    return size/1024/1024

print()
print("Complete!")
print()
print("download size : " + "%.2f" % getFileSize(filePath) + " MB")
print()
print("file_success_num :",file_success_num)
print()
print("file_failed_num :",file_failed_num)
print()
print("use time :" + "%.2f" % end + " s")

os.system("pause")
