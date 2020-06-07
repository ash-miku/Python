#
# json = {"code":0,"message":"0","ttl":1,"data":{"aid":498383279,"bvid":"BV1NK411p7fK","view":1224060,"danmaku":1800,"reply":2674,"favorite":2910,"coin":7135,"share":3033,"like":90239,"now_rank":0,"his_rank":0,"no_reprint":1,"copyright":1,"argue_msg":"","evaluation":""}}
# #s = str(json)
# data = json["data"]
# aid = data["aid"]
# bvid = data["bvid"]
# view = data["view"]
# print(type(json))

import random
# num = 0
for i in range(0,100):
    num = random.randint(0,100000000)
    urls="https://api.bilibili.com/x/web-interface/archive/stat?aid="+str(num)
    print(urls)