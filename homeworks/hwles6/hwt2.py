"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
m = 25
l = 15
class Road:
    def __init__(self, _lenght, _width):
        Road.lenght = _lenght
        Road.width = _width

    def  mass(self, _lenght, _width, m, l):
        result = _lenght * _width * m * l
        return result

r = Road( 100, 10000)
print(Road.mass(r, 100, 10000, m, l))