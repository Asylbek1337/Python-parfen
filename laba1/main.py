myList = [13, 46, 79, 85, 95]   # вектор

print(myList)

с = set(myList)
print(с)

r = list(с)
print(r)
print("----------------------------------------------------------------------------------")

b = [100, 34, 46, 52, 34]

d = [1 , 0, 0 , 0]

d[0] = r[0]*b[0]
print('d:',d)


# print(type(с))  # выводит тип данных переменной

# ДЗ: 1. Попробуйте сохранить в одной переменной следующий вектор: 13, 46, 79, 85, 95.
#     2. Реализуйте умножение вектора из 1 на: 100, 34, 46, 52, 34.