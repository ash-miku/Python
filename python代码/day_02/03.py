import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np

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

midwest = pd.read_csv("./midwest_filter.csv")#导入数据
pop = midwest[midwest["PID"] == 562]#选择第562号数据
pop_agekind = ["percchildbelowpovert","percadultpoverty","percelderlypoverty"]#数据种类

popperc = ((np.array(pop[pop_agekind])).tolist())[0]#数字数据比例
plt.axes(aspect=1)#椭圆形状
plt.pie(x=popperc,labels=pop_agekind,autopct='%3.1f %%')#数据类型
#标题设置
plt.title("ALEXANDER 贫困人口年龄比例")
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#标签设置
plt.legend(loc="lower left",fontsize=10,bbox_to_anchor=(1.1,0.75),borderaxespad=0.3)
# loc =  'upper right' 位于右上角
# bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边，精准位置
# ncol=2 分两列
# borderaxespad = 0.3图例的内边距
plt.show()
