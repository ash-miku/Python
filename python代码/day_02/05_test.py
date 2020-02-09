"""
Numpy运算和通用函数
"""
list = [1,20,28,37,18,56]
#循环
#特殊的语法
[i*3 for i in list]
import numpy as np
a1 = np.arange(0,10)
#如果使用Numpy的话，以及进行矢量和标量之间的运算
#a[矢量] * 3[标量]
a1 = np.arange(10).reshape((2,5))
#高维空间的矢量和标量运算可以吗？
#目前来看，矢量和标量运算支持高位空间运算的，并且支持四则运算
b1  = a1 +10
#矢量和矢量之间可以运算吗
#如果两个矢量的维度相同的话，每个矢量的对应位置元素进行计算
a1.shape == b1.shape
# def test():
#     if a.shape == b.shape :
#         计算
#     else :
#         抛出异常，或者提示用户
a1 + b1
a1 - b1
a1 * b1
a1 / b1

#维度不同的话，能进行计算吗
a1
m = np.arange(5)
"""
a  (2,5)
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
m (5,)
array([0, 1, 2, 3, 4])
a + m
array([[ 0,  2,  4,  6,  8],
       [ 5,  7,  9, 11, 13]])
"""
n = np.arange(1,3).reshape((-1,1))
a1 + n
"""
广播机制：上面学习的标量和矢量的运算、矢量和矢量的运算是shape都相同的情况下
          a.shape != b.shape，但是其中有一个维度是相同的，这种场景是广播机制进行运算的
(2,1)
np.arange(1,3).reshape((-1,1))
array([[1],
       [2]])
a (2,5)
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
a + n 
array([[ 1,  2,  3,  4,  5],
       [ 7,  8,  9, 10, 11]])
"""
"""
比较运算和逻辑运算
"""
#使用每个数组的对应位置进行比较运算、返回一个bool类型新的数组
np.array([6,4,3]) > np.array([9,5,11])
#逻辑运算符 and / or / not
#logical_or / and / not
np.logical_or(np.array([False,True])
              ,np.array([True,False]))
x = 3
y = 5
x < y and x > y

a2 = np.array([3,6,9])
b2 = np.array([4,5,8])
#numpy的ndarray数组目前是不允许直接使用逻辑运算符的
np.any(a2<b2) and np.any(a2>b2)
np.all(a2<b2)
(a2<b2).all()

#构建测试数据集
#通用函数
alpha = np.linspace(-1,1,11)
y = np.sin(np.pi * alpha)#
"""
sin(参数) --->  返回值 
sin , cos , tan 三角函数
sqrt 求平方根
np.log (默认以e为底)，log2 , log10
np.exp 计算自然指数
反三角函数  arc + sin/cos/tan
双曲三角函数  sin/cos/tan + h 
"""
"""
二元函数
运算函数 ： np.add(参数1，参数2)
"""
"""
Numpy ：ML 【】
Numpy : 绘制可视化图【答辩】
        3小问题 90
        2小问题 80
        1小问题 70 
        0小问题 [50-70]

机器学习：决策树 - 90
 
Pandas
 
"""
















