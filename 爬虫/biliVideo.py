import requests
import csv
import time
import os
import random

# 获取网页
id = input("请输入爬取视频数量:")
# num = 0
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

for i in range(0,int(id)):
    num = random.randint(0,100000000)
    urls="https://api.bilibili.com/x/web-interface/archive/stat?aid="+str(num)
    #{"code":0,"message":"0","ttl":1,"data":{"aid":540931451,"bvid":"BV1Ri4y1s7Am","view":204266,"danmaku":377,"reply":1452,"favorite":385,"coin":102,"share":950,"like":12343,"now_rank":0,"his_rank":0,"no_reprint":1,"copyright":1,"argue_msg":"","evaluation":""}}
    r = requests.get(urls,headers = headers)
    json = r.json()
    code = json['code']
    if code == 0:
        data = json['data'] #拿出子字典
        # 通过字典获取各数据
        list = []
        aid = str(data['aid'])   #视频av号
        list.append(aid)
        bvid = str(data['bvid']) #视频bv号
        list.append(bvid)
        view = str(data['view']) #观看次数
        list.append(view)
        danmaku = str(data['danmaku'])   #弹幕数
        list.append(danmaku)
        favorite = str(data['favorite']) #收藏数
        list.append(favorite)
        coin = str(data['coin']) #投币数
        list.append(coin)
        share = str(data['share'])   #分享数
        list.append(share)
        like = str(data['like']) #点赞数
        list.append(like)
        #print(aid,bvid,view,danmaku,like,coin,favorite,share)
        #print(type(bvid))
        print(list)

        #创建保存路径
        if not os.path.exists('biliVideo'):

            os.mkdir('biliVideo')

        with open("biliVideo/biliVideo_" + str(id) + ".csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(list)
            print("写入成功")

    r.close()

    time.sleep(2)
    # time.sleep(random.randint(2, 4))
print()
print("Complete !")
