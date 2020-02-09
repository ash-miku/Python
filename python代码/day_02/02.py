import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


midwest=pd.read_csv("./midwest_filter.csv")
categories=np.unique(midwest['category'])#去重
plt.figure(figsize=(16,10))#绘图尺寸

for i in range(len(categories)):
    plt.scatter(midwest.loc[midwest["category"]==categories[i],"area"],#取出x值
                midwest.loc[midwest["category"]==categories[i],"popadults"],#取出y值
                s=midwest.loc[:,"popasian"],#根据popasian改变点的大小
                c=np.array(plt.cm.tab10(i/len(categories))).reshape(1,-1),#随机赋予颜色
                label=categories[i],
                alpha=0.8,linewidths=0.8)#图像透明度与点外圈线的宽度
plt.gca().set(xlabel='area', ylabel='popadults')#坐标轴标题
plt.xticks(fontsize=12)#标尺的字的大小
plt.yticks(fontsize=12)
plt.title("The relationship between the proportion of Asian adults and regional area", fontsize=22)
plt.legend(fontsize=12
           ,markerscale=0.45 #现有的图例气泡的比例
          )
plt.show()
