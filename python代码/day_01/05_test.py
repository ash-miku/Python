#定义一个boolean类型的变量 has_ticket 表示是否有车票
has_ticket = False
#定义整型变量 knife_length ，表示刀的长度
#相同的代码块首行缩进要保持一致
#不同的代码块，首行缩进可以不一致的
knife_length = 10
if has_ticket :
    print("您有车票...可以去安检...")
    if knife_length > 20 :
        print("您带的刀具太长了,有 %d 公分长 " % knife_length)
        print("不允许上车")
    else :
        print("安检通过，祝旅行愉快......")
else :
           print("去买票去吧...")









