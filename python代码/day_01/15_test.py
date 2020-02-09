"""
函数什么时候需要返回值呢？
一般是函数的处理结果需要被程序使用时，才会使用return返回“数据”
"""
def add(num1 , num2) :
    return num1 + num2
sum_result = add(1,2)
print("计算结果： %d" % sum_result)