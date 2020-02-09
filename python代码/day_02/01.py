import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

midwest=pd.read_csv('./midwest_filter.csv') #提取数据集内容
x=np.array(midwest['county'])   #使用array数组获取数据集列名为"county"的数据
y=np.array(midwest['poptotal'])
plt.title("各国家总人口折线图")  #折线图标题
plt.rcParams['font.sans-serif']=['SimHei']  #解决中文标题乱码
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x[:5],y[:5],color="#39C5BB",lw=5)   #提取x,y前五个数值并绘制为折线图
plt.show()


