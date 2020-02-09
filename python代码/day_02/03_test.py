# 数组的索引和切片
import numpy as np

"""
索引是数字
"""
# a.ndim对象的属性 , np.ndim(a) numpy的方法
a = np.arange(24).reshape((2, 3, 4))
a[1]
a[1][0][0]  # 12
b = np.arange(5)  # [0,1,2,3,4]
b.shape
b[3]
c = np.arange(12).reshape((3, 4))
c[1]
c[1][2]
c[1, 2]  # 变种的写法
c[(1, 2)]  # 变种的写法
# 修改数值
b[3] = 300
c[1] = 100
"""
索引是列表
"""
three = b[0], b[1], b[2]
three2 = b[[0, 1, 2]]  # 索引是列表
# 列表里面可以是一个元素
t = b[[0]]
"""
b:[0,1,2,3,4]
three2:[0,1,3]
three2[1] = 100 
打印 : three2  0 ，100， 3
原数组打印：[0,1,2,3,4]
说明：使用列表进行索引得到数据和原数组不占用同样的内存空间
"""
c = np.arange(12).reshape((3, 4))
c[[0, 2]]
c[[0, 2], [1, 2]]
c[0, 1], c[2, 2]
c[0, 1], c[2, 2]

# 下标数组(numpy数组类型的)
v = np.array([0, 1, 2])
r = b[v]  # class 'numpy.ndarray
# --------- #
t1 = b == 2  # 返回了ndarray数组，数组里面的元素都是bool类型
b[t1]  # 参数是数组
"""
for i in b :
    A.append(True)
else :
    A.append(False)
"""
e = np.arange(10).reshape((2, 5))
# e.shape = (2,5) 两行五列
# e.ndim # 2 维度
# e.size  #10
# 返回一个列表：列表中的数据必须是偶数
# array[0,2,4,6,8]
"""
array([[ True, False,  True, False,  True],
       [False,  True, False,  True, False]])
"""
t2 = e % 2 == 0
e[t2]

t3 = np.array([False, True])
"""
t2 没有和 e一一对应，这种场景返回什么数据呢
广播机制：pandas
"""
e[t3]
"""
要索引出所有数值大于6的数据
"""
e[e > 6]
"""
1.数值型索引
2.列表索引
3.数组索引
"""

"""
切片
"""
a1 = np.arange(10, 20)  # 左闭右开区间
"""
索引：一般根据指定位置进行获取值
切片：一般根据范围进行获取值
"""
b1 = a1[2:8]  # 使用：
"""
索引：通过原数组（a）索引出来数组（b）      
       修改b数组中的数值，不会影响到a数组，
      因为它们两个数组不共用同一个内存空间
切片：
      通过原数组（a）切片出来的数组（b）
      如果修改b中的数组，会对原数组（a）发生改变
      因为这两个数组公用同一个内存空间
"""

a1[:: 2]  # a[t1:t2:t3] ,从t1开始到t2结束，步长为t3
a1[3:]  # a[t1:t2]从哪里开始，结束的位置没有写的话，那么就是一直到最后一个元素
a1[::-1]  # 逆序输出原数组
a1[: 6: 3]  # [t1,t2,t3],t1不写的话代表从头开始切片

# 广播机制 | 3D图形
b2 = np.arange(0, 60, 10).reshape(-1, 1) \
     + np.arange(0, 6)
b2[1:4]
"""
索引 ： [（1,2）,(4,5)]
切片：第一维度获取1:4数据，之后从1:4这个数据里面进行2:5切片
"""
b2[1:4, 2:5]
"""
首先打印：b[0]
接下来：[t1,t2:t3],t1代表第一个维度获取那些数据
        t2,t3代表从上面获取的子集数据从哪里切片到哪里结束
        如果只写：,那么代表从[0,length-1]
"""
b2[1, :]
b2[:, 2]
# t1，t2 | 逗号前是索引第一个维度，逗号后面是索引第二个维度
b2[0:2, 0:2]
b2[::2, ::2]
# [t1,t2] t1从第一个维度进行切片，t2一个列表，代表要那一列的数据
b2[:3, [0, 3]]  # 带有指定列的切片
"""
1.现根据0轴的要求进行切片
   然后将结果根据1轴的要求进行切片
2.对原数组的0轴和1轴都进行切片，最后将数据取交集
"""
