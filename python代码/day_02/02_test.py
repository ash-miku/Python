#创建数组
import numpy as np
a = np.array([1,2,3,4])
b = np.array([1,2,3,4],dtype=float)
da = np.array([
    [1,2,3,4] ,
    [5,6,7,8] ,
    [9,10,11,12]
])
#ndmin是创建数组的时候，指定数组的维度
db = np.array([1,2,3,4,5,6,7,8],ndmin=2)
dc = np.array([1,2,3,4,5,6,7,8])
"""
用函数创建数组
"""
#zeros创建的元素都是0，里面传递的参数代表了数组的维度
t = np.zeros((2,10))
"""
asarray ：输入的参数列表[1,2,3]，元组（1,2）
          返回一个数组，ndarray
（）arange : 从开始值到结束值根据一定的步长创建数组
（）ones :创建元素值全是1
empty:创建的数组没有填充任何元素，但是分配了内存空间
eye:对角线元素全是1，其余元素都是零
diag:对角线元素值是可以指定的，其余元素全是0的二维数组
（）linspace：从开始值到结束值，根据元素数量 创建等差数列的数组
"""
#同一种元素的数组
t = np.ones((6,)) # (1,6)创建数组的维度
t = np.ones(6)
t = np.ones(da.shape) # 创建三行四列的数组
t = np.ones_like(da) # ndarray
t = np.ones_like(da,dtype=np.float)
#np.ones() / np.zeros() / np.empty()
#创建的都是1,0，空（但是内存空间是分配的）
#矢量和标量的运算：矢量：np.ones_like(da)|标量：6.4
df = 6.4 * np.ones_like(da)
#按照指定规则进行填充数据
t = np.full(da.shape,6.4)

#对角线独特的数组
t = np.eye(4 , dtype=int)
t = np.eye( 4, dtype = int , k = 1 )
t = np.eye( 4, dtype = int , k = -1 )
#创建单位矩阵，但是函数不能调整对角线
t = np.identity(4)
#
t = np.diag([1,2,3,4])#4行4列，数据在对角线
t = np.diag([1,2,3,4],k=2)#可以调整对角线的位置
de = np.arange(16).reshape((4,4))
t = np.diag(de)
t = np.diag(de,k=1)
#[1, 3, 5, 7, 9] 左闭右开区间 | 步长
t = np.arange(1,10,3)










