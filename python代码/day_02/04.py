import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

midwest=pd.read_csv('./midwest_filter.csv')
row=midwest[midwest['PID']==561]#筛选只要PID为561的一行
x=['popblack','popamerindian','popasian','popother']
y=(np.array(row[x])).reshape(4,)#取出x轴对应的数据
plt.gca().set(xlabel='race', ylabel='Number')#坐标轴标题
plt.xticks(fontsize=12)#标尺的字的大小
plt.yticks(fontsize=12)
plt.title("Number of races in ADAMS", fontsize=22)#大标题
plt.bar(x,y,0.5,color="rgby")
plt.show()
