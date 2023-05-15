#Перепишите элементы данного массива в новый массив,
# помещая в него сначала все отрицательные, затем нулевые и, нако¬нец, положительные элементы.

num = [-1, 23, -35, -54, 0, 233, -7, -1023, -342, 234]
plus, minus, zero = [], [], []
for i in num:
    if i < 0:
        minus.append(i)
    elif i == 0:
        zero.append(i)
    else:
        plus.append(i)
num = [-1, 23, -35, -54, 0, 233, -7, -1023, -342, 234]
num = list(filter(lambda x: x < 0, num)) + list(filter(lambda x: x == 0, num)) + list(filter(lambda x: x > 0, num))
print(num)