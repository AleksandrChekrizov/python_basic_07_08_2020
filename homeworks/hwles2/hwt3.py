"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
y_list = ['зима', 'весна', 'лето', 'осень']
y_dict = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}
while True:
    m = input('введите месяц в виде целого числа от 1 до 12')
    if type(m) == float or type(m) == bool or type(m) == str:
        print('ошибка ввода')
    elif int(m) == 0:
        print('ошибка ввода')
    elif int(m) < 0:
        print('ошибка ввода')
    elif int(m) > 12:
        print('ошибка ввода')

    else:
        break

m = int(m)
if m == 12 or m <= 2:
    print(y_list[0])
    print(y_dict.get(1))
elif m > 2 and m <=5:
    print(y_list[1])
    print(y_dict.get(2))
elif m > 5 and m <= 8:
    print(y_list[2])
    print(y_dict.get(3))
elif m > 8 and m <=11:
    print(y_list[3])
    print(y_dict.get(4))