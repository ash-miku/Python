"""
功能：打印某一个字符多少次
"""
def print_line(char,times):
    """ 打印多行的分割线
    :param char: 分割线使用的字符
    :param times:分割线打印的次数
    """
    row = 0
    while row < 5 :
        print(char * times)
        row += 1
print_line("-",3)