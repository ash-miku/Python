"""
除了3之外，全部打印
"""
i = 0
while i <= 10 :
    if i == 3 :
        i += 1
        continue
    print(i)
    i += 1
print("over")