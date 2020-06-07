import requests
import csv
import time
import os
import random
import re


def bilibili_Video():
    # 获取网页
    id = input("请输入爬取视频数量:")
    # num = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    # 创建保存路径
    if not os.path.exists('biliVideo'):
        os.mkdir('biliVideo')

    # 提前打开文件创建列名
    with open("biliVideo/biliVideo_" + str(id) + ".csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["视频av号", "视频bv号", "观看次数", "弹幕数",
                         "收藏数", "投币数", "分享数", "点赞数"])

    for i in range(0, int(id)):
        num = random.randint(0, 100000000)
        urls = "https://api.bilibili.com/x/web-interface/archive/stat?aid=" + \
            str(num)
        # {"code":0,"message":"0","ttl":1,"data":{"aid":540931451,"bvid":"BV1Ri4y1s7Am","view":204266,"danmaku":377,"reply":1452,"favorite":385,"coin":102,"share":950,"like":12343,"now_rank":0,"his_rank":0,"no_reprint":1,"copyright":1,"argue_msg":"","evaluation":""}}
        r = requests.get(urls, headers=headers)
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']  # 拿出子字典
            # 通过字典获取各数据
            list = []
            aid = str(data['aid'])  # 视频av号
            list.append(aid)
            bvid = str(data['bvid'])  # 视频bv号
            list.append(bvid)
            view = str(data['view'])  # 观看次数
            list.append(view)
            danmaku = str(data['danmaku'])  # 弹幕数
            list.append(danmaku)
            favorite = str(data['favorite'])  # 收藏数
            list.append(favorite)
            coin = str(data['coin'])  # 投币数
            list.append(coin)
            share = str(data['share'])  # 分享数
            list.append(share)
            like = str(data['like'])  # 点赞数
            list.append(like)
            # print(aid,bvid,view,danmaku,like,coin,favorite,share)
            # print(type(bvid))
            print(list)

            with open("biliVideo/biliVideo_" + str(id) + ".csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(list)
                print("写入成功")
        else:
            print()
            print("视频不存在！")
            print()

        r.close()

        time.sleep(2)
        # time.sleep(random.randint(2, 4))
    print()
    print("Complete !")


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

        print("查询成功！")
        print()
        print("UID : "+mid)
        print("昵称 : "+name)
        print("性别 : "+sex)
        print("个性签名 : "+sign)
        print("账号等级 : "+level)
        print("生日 : "+birthday)
        print("bilibili认证 : "+role+" "+title)
        print("会员类型 : "+vipType)
        print("会员状态 : "+vipStatus)
        print()
    else:
        print()
        print("用户不存在！")
        print()


if __name__ == '__main__':
    while 1:
        print("欢迎打开新世界的大门！")
        print()
        print("1.随机爬取B站视频数据")
        print("2.爬取某UP主相簿照片")
        print("3.查询UP主基本信息")
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
        elif switch_num == "0":
            print("Bye~")
            break
        else:
            print("输入的序号有误，请重新输入！")
            print()
