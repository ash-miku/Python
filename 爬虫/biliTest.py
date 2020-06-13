import requests
import csv
import time
import os
import random
import re
import pymysql
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def bilibili_Video():
    # 获取网页
    numid = input("请输入爬取视频数量:")
    # num = 0
    success_num = 0
    fail_num = 0

    headers = {
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    # 创建保存路径
    if not os.path.exists('biliVideo'):
        os.mkdir('biliVideo')
    elif os.path.exists('biliVideo'):
        try:
            os.remove('biliVideo/biliVideo_' + str(numid) + '.csv')
        except:
            print()
            print("删除的文件不存在")
            print()
        else:
            print()
            print("删除文件成功")
            print()

    # 提前打开文件创建列名
    with open("biliVideo/biliVideo_" + str(numid) + ".csv", "a", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["视频av号", "视频bv号", "视频分区", "视频标题", "作者昵称", "作者UID", "视频通过审核时间", "观看次数", "弹幕数",
                         "收藏数", "投币数", "分享数", "点赞数"])

    for i in range(0, int(numid)):
        num = random.randint(0, 100000000)
        urls = "http://api.bilibili.com/x/web-interface/view?aid=" + \
            str(num)
        r = requests.get(urls, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            stat = data['stat']  # 拿出stat子字典
            owner = data['owner']   # 拿出owner子字典
            # 通过字典获取各数据
            list = []
            aid = str(stat['aid'])  # 视频av号
            list.append(aid)
            bvid = str(data['bvid'])  # 视频bv号
            list.append(bvid)
            tid = data['tid']  # 视频分区id
            if tid in [1, 24, 25, 47, 86, 27]:
                tname = "动画"
            elif tid in [13, 33, 32, 51, 152]:
                tname = "番剧"
            elif tid in [167, 153, 168, 169, 195, 170]:
                tname = "国创"
            elif tid in [3, 28, 31, 30, 194, 59, 193, 29, 130]:
                tname = "音乐"
            elif tid in [129, 20, 198, 199, 200, 154, 156]:
                tname = "舞蹈"
            elif tid in [4, 17, 171, 172, 65, 173, 121, 136, 19]:
                tname = "游戏"
            elif tid in [36, 201, 124, 207, 208, 209, 122]:
                tname = "知识"
            elif tid in [188, 95, 189, 190, 191]:
                tname = "数码"
            elif tid in [160, 138, 21, 76, 75, 161, 162, 163, 176, 174]:
                tname = "生活"
            elif tid in [119, 22, 26, 126, 127]:
                tname = "鬼畜"
            elif tid in [155, 157, 158, 164, 159, 192]:
                tname = "时尚"
            elif tid in [202, 203, 204, 205, 206]:
                tname = "资讯"
            elif tid in [5, 71, 137, 131]:
                tname = "娱乐"
            elif tid in [181, 182, 183, 85, 184]:
                tname = "影视"
            elif tid in [177, 37, 178, 179, 180]:
                tname = "纪录片"
            elif tid in [23, 147, 145, 146, 83]:
                tname = "电影"
            elif tid in [11, 185, 187]:
                tname = "电视剧"
            list.append(tname)
            title = str(data['title'])  # 视频标题
            list.append(title)
            name = str(owner['name'])   # 视频作者
            list.append(name)
            mid = str(owner['mid'])  # 作者UID
            list.append(mid)
            ctime = int(data['ctime'])  # 视频通过审核时间

            # 时间戳转换
            ctimeArray = time.localtime(ctime)
            ctimeStyleTime = time.strftime("%Y-%m-%d-%H:%M:%S", ctimeArray)

            list.append(ctimeStyleTime)
            view = str(stat['view'])  # 观看次数
            list.append(view)
            danmaku = str(stat['danmaku'])  # 弹幕数
            list.append(danmaku)
            favorite = str(stat['favorite'])  # 收藏数
            list.append(favorite)
            coin = str(stat['coin'])  # 投币数
            list.append(coin)
            share = str(stat['share'])  # 分享数
            list.append(share)
            like = str(stat['like'])  # 点赞数
            list.append(like)
            # print(aid,bvid,view,danmaku,like,coin,favorite,share)
            # print(type(bvid))
            print(list)

            # 将数据写入本地csv文件
            # with open("biliVideo/biliVideo_" + str(id) + ".csv", "a", encoding='utf-8', newline='') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(list)
            #     print("写入成功")

            # 将数据写入云数据库
            try:
                connent = pymysql.connect(host='miku-miku.top', port=3306,
                                          user='root', passwd='ly231930', db='bilibili', charset='utf8')
                cursor = connent.cursor()
                sql = "replace into bilibili_Video values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(list[0]), str(list[1]), str(list[2]), pymysql.escape_string(str(
                    list[3])), pymysql.escape_string(str(list[4])), str(list[5]), str(list[6]), str(list[7]), str(list[8]), str(list[9]), str(list[10]), str(list[11]), str(list[12]))
                # print(sql)
                cursor.execute(sql)
                connent.commit()
                cursor.close()
                connent.close()
                success_num += 1
                print()
                print("数据库写入成功,已完成{0}/{1}......{2:.2%}".format(success_num,int(numid),int(success_num)/int(numid)))
            except:
                print("写入失败")
                fail_num += 1
        else:
            print()
            print("视频不存在！")
            success_num += 1
            print()

        r.close()

        time.sleep(2)
        # time.sleep(random.randint(2, 4))
    print()
    print("Complete !")
    print("数据库写入失败次数 : %d" % fail_num)


def bilibili_Album():
    # import requests
    # import re
    # import os
    # import time

    # 获取网页
    uid = input("请输入B站用户uid:")
    print("uid is :", uid)
    page_num = input("请输入想要爬取相簿页数:")
    print("Total page num is :", page_num)
    print()
    print("Start------")
    print()

    start = time.time()

    num = 0
    file_success_num = 0
    file_failed_num = 0

    for i in range(0, int(page_num)):
        url = "https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=" + str(uid) + "&page_num=" + str(
            num) + "&page_size=30&biz=all"
        num = num + 1
        r = requests.get(url)
        newurl = r.text.replace('\\', '')

        # 解析网页
        urls = re.findall(
            'http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            newurl)
        # print(urls)
        # print(newurl)

        # 创建保存路径
        if not os.path.exists('bilibili/' + str(uid)):
            os.makedirs('bilibili/' + str(uid))

        # 保存图片
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

        for url in urls:

            file_name = url.split('/')[-1]

            r = requests.get(url, headers=headers)

            if (str(r) == "<Response [200]>"):
                with open('bilibili/' + str(uid) + '/' + file_name, 'wb') as f:
                    f.write(r.content)
                file_success_num += 1
                print("正在下载:", file_name)
            else:
                print("正在下载: ---------------404 NOT FOUND----------------")
                file_failed_num += 1

    end = time.time() - start

    filePath = "bilibili/" + str(uid)

    # 显示下载文件大小
    def getFileSize(filePath, size=0):
        for root, dirs, files in os.walk(filePath):
            for f in files:
                size += os.path.getsize(os.path.join(root, f))
                # print(f)
        return size / 1024 / 1024

    print()
    print("Complete!")
    print()
    print("download size : " + "%.2f" % getFileSize(filePath) + " MB")
    print()
    print("file_success_num :", file_success_num)
    print()
    print("file_failed_num :", file_failed_num)
    print()
    print("use time :" + "%.2f" % end + " s")


def bilibili_Info():

    uid = input("请输入B站用户uid:")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    # 创建保存路径
    if not os.path.exists('biliInfo'):
        os.mkdir('biliInfo')

    # 提前打开文件创建列名
        with open("biliInfo/biliInfo.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["UID", "昵称", "性别", "个性签名",
                             "账号等级", "生日", "bilibili认证", "认证标题", "会员类型", "会员状态"])

    urls = "https://api.bilibili.com/x/space/acc/info?mid="+str(uid)
    r = requests.get(urls, headers=headers)
    json = r.json()
    # print(json)
    code = json['code']
    if code == 0:
        # 拿出data子字典
        data = json['data']
        mid = str(data['mid'])
        name = str(data['name'])
        sex = str(data['sex'])
        sign = str(data['sign'])
        level = str(data['level'])
        birthday = str(data['birthday'])
        # 拿出official子字典
        official = data['official']
        role = str(official['role'])
        title = str(official['title'])
        # 拿出vip子字典
        vip = data['vip']
        vipType = str(vip['type'])
        vipStatus = str(vip['status'])

        # 个性签名状态
        if sign == "":
            sign = "无"

        # bilibili认证类型
        if role == "0":
            role = "无"
        elif role == "1":
            role = "bilibili个人认证"
        else:
            role = "bilibili企业认证"

        # 认证标题
        if title == "":
            title = "无"

        # bilibili会员类型
        if vipType == "0":
            vipType = "普通会员"
        elif vipType == "1":
            vipType = "大会员"
        elif vipType == "2":
            vipType = "年度大会员"

        # 会员状态
        if vipStatus == "0":
            vipStatus = "否"
        elif vipStatus == "1":
            vipStatus = "是"

        # 创建写入列表
        list = []
        list.append(mid)
        list.append(name)
        list.append(sex)
        list.append(sign)
        list.append(level)
        list.append(birthday)
        list.append(role)
        list.append(title)
        list.append(vipType)
        list.append(vipStatus)

        # 文件写入
        with open("biliInfo/biliInfo.csv", "a+", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(list)

        print("查询成功！")
        print()
        print("UID : "+mid)
        print("昵称 : "+name)
        print("性别 : "+sex)
        print("个性签名 : "+sign)
        print("账号等级 : "+level)
        print("生日 : "+birthday)
        print("bilibili认证 : "+role)
        print("会员类型 : "+vipType)
        print("会员状态 : "+vipStatus)
        print()
    else:
        print()
        print("用户不存在！")
        print()

def bilibili_Chart():

    headers = {
            'Connection': 'close',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    rid1 = [24, 25, 47, 86, 27]
    nums = []
    num1 = 0
    for test in rid1:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num1 += count
    nums.append(num1)

    rid2 = [157, 158, 164, 159, 192]
    num2 = 0
    for test in rid2:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num2 += count
    nums.append(num2)

    rid3 = [71, 137, 131]
    num3 = 0
    for test in rid3:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num3 += count
    nums.append(num3)

    rid4 = [28, 31, 30, 194, 59, 193, 29, 130]
    num4 = 0
    for test in rid4:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num4 += count
    nums.append(num4)

    rid5 = [20, 198, 199, 200, 154, 156]
    num5 = 0
    for test in rid5:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num5 += count
    nums.append(num5)

    rid6 = [17, 171, 172, 65, 173, 121, 136, 19]
    num6 = 0
    for test in rid6:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num6 += count
    nums.append(num6)

    rid7 = [201, 124, 207, 208, 209, 122]
    num7 = 0
    for test in rid7:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num7 += count
    nums.append(num7)

    rid8 = [95, 189, 190, 191]
    num8 = 0
    for test in rid8:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num8 += count
    nums.append(num8)

    rid9 = [138, 21, 76, 75, 161, 162, 163, 176, 174]
    num9 = 0
    for test in rid9:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num9 += count
    nums.append(num9)

    rid10 = [182, 183, 85, 184]
    num10 = 0
    for test in rid10:
        url = "http://api.bilibili.com/x/web-interface/newlist?rid="+str(test)+"&pn=1&ps=1"
        r = requests.get(url, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出data子字典
            page = data['page']
            count = page['count']
            num10 += count
    nums.append(num10)
    
    print(nums)
    #画板设置
    large=22;med=16;small=12;
    params = {'axes.titlesize': large,
            'legend.fontsize': med,
            'figure.figsize': (12, 6),
            'axes.labelsize': med,
            'xtick.labelsize': med,
            'ytick.labelsize': med,
            'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')

    pop_agekind = ["动画","时尚","娱乐","音乐","舞蹈","游戏","知识","数码","生活","影视"]#数据种类

    plt.axes(aspect=1)#椭圆形状
    plt.pie(x=nums,labels=pop_agekind,autopct='%3.1f %%')#数据类型
    #标题设置
    plt.title("BILIBILI(B站)各分区视频比例")
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #标签设置
    plt.legend(loc="lower left",fontsize=12,bbox_to_anchor=(1.3,0.4),borderaxespad=0.3)
    # loc =  'upper right' 位于右上角
    # bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边，精准位置
    # ncol=2 分两列
    # borderaxespad = 0.3图例的内边距
    plt.show()


if __name__ == '__main__':
    while True:
        print("欢迎打开新世界的大门！")
        print()
        print("1.随机爬取B站视频数据")
        print("2.爬取某UP主相簿照片")
        print("3.查询UP主基本信息")
        print("4.查询各分区视频比例")
        print()
        print("0.退出程序")
        print()
        switch_num = input("请选择功能:")
        if switch_num == "1":
            bilibili_Video()
            break
        elif switch_num == "2":
            bilibili_Album()
            break
        elif switch_num == "3":
            bilibili_Info()
            break
        elif switch_num == "4":
            print("正在查询,请稍后...")
            bilibili_Chart()
            break
        elif switch_num == "0":
            print("Bye~")
            break
        else:
            print("输入的序号有误，请重新输入！")
            print()
