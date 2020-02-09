"""
一个函数里面是可以嵌套别的函数的
"""
def test1():
    print("*" * 10)

def test2():
    print("-" * 10)
    test1()
    print("-" * 10)

test2()