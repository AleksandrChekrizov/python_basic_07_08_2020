""" 2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

name = str(input('имя:'))
sn = str(input('фамилия:'))
by = str(input('год рождения:'))
city = str(input('город проживания:'))
em = str(input('email:'))
pn = str(input('телефон:'))

def data_f(a, b, c, d, e, f):
    res = dict({'имя:':a, 'фамилия:': b, 'год рождения:':c, 'город проживания:':d, 'email:':e, 'телефон:':f})
    return res

info = data_f(name, sn, by, city, em, pn)
print(info)