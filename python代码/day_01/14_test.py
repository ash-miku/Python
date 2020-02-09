#函数就是封装了一段代码/函数必须主动调用，否则不会执行的
def say():
    print("hello 1")
    print("hello 2")
    print("hello 3")

def add(num1 , num2) :
    # return num1 + num2
    result = num1 + num2
    print("%d + %d = %d" % (num1 ,num2 ,result))

add(1,2)

