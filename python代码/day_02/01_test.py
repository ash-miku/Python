"""
numpy是python语言的第三方库，被广泛应用与数据分析领域
它主要实现了高维数组和矩阵之间的运算
以后想学习ML,DL,numpy是必须会的
"""
"""
数组对象基础
"""
import numpy as np
# print(np.__version__)
#首先认识一下数组对象
data = np.array([1,2,3,4,5])
#dir(data) | 没有交互式命令行的话,print(dir(data))
#当前对象的类型 | type(data)
#查看数组元素的类型 | data.dtype
#int/int8/int16(32)(64)|bool|float|string_
#int8有符号的整型，int8主要表示长度为8位,能够表示多大的数字：-128~127
#一个数组对象怎么把内部元素转化成float类型呢
new_data = data.astype(np.float)
#数组的外貌
new_data.shape # (5,) 第一个维度有多少个元素
new_data.size # 5 整个数组里面有多少个元素
new_data.ndim # 1 代表数组的维度




