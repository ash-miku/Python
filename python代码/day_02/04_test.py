"""
针对数组的操作：
1.变形
2.组合
3.切割
"""
import numpy as np
a = np.arange(10)
#reshape(参数)：参数为元组，功能修改ndarray数组的形状
b = np.arange(10).reshape((2,5))
# np.reshape(a,(2,5))
#（-1,1）第二个维度只有一个元素，第一个维度有多少行不关心
c = np.reshape(b,(-1,1))
c1 = np.reshape(b,(-2,1))
t = np.reshape(b,(10,))
t1 = np.reshape(b,(1,10))
b.shape = (1,10)#修改数组的形状的第二种方法
p = b.flatten() #数据变成一位，数据打平,对原数组没有影响
ne = np.ravel(b)#打平数据，修改新生原数组元素对之前的数组是有影响的
data = np.arange(0,5)
c2 = data[: , np.newaxis] #这个写法和下面是等价的
c3 = data[:,None]
d = data[np.newaxis,:]
# axis=0 | axis
data2 = np.expand_dims(data,axis = 0 )
data3 = np.expand_dims(data,axis = 1 )
#数组的组合和分割
a1 = np.arange(9).reshape(3,3)
b1 = np.arange(12).reshape(3,4)
c4 = np.arange(15).reshape(3,5)
np.hstack((a1,b1)) #水平组合
np.hstack((a1,b1,c4))
np.concatenate((a1,b1),axis=1)
m = a1 * 3
a1.shape == m.shape
np.stack((a1,m),axis=1)
#数组的分割
a2 = np.arange(24).reshape((4,6))
t2 = np.split(a2,2,axis=1)
t3 = np.split(a2,2,axis=0)
t4 = np.hsplit(a2,2)
t5 = np.vsplit(a2,2)












