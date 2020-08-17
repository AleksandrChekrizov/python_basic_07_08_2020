"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
a = float(input('введите 1е число:'))
b = float(input('введите 2е число:'))
c = float(input('введите 3е число:'))

def my_func(v1, v2, v3):
    if (v1 >= v2 >= v3):
        res = v1 +v2
    elif (v1 <= v2 <= v3):
            res = v3 +v2
    elif (v1 >= v2 <= v3):
        res = v1 +v3
    elif (v1 <= v2 >= v3):
        if (v1 >= v3):
            res = v2 + v1
        else:
            res = v2 +v3
    return res
i = my_func(a, b,c)
print(i)
