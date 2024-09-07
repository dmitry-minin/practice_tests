"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import datetime


class Car:
    def __init__(self, brand, model, year_of_production):
        self.brand = brand
        self.model = model
        if type(year_of_production) is not int:
            raise TypeError(f'Год выпуска должен быть числом, а ты ввел хуйню {year_of_production}')
        elif year_of_production > datetime.now().year:
            raise ValueError(f'{year_of_production} вы ввели. Эта машина еще не была выпущена')
        elif year_of_production < datetime.now().year - 150:
            raise ValueError(f'{year_of_production} вы ввели. Эта машина - скорее лошадь')
        self.year_of_production = year_of_production


# код для проверки
#car = Car('Toyota', 'Corolla', 2022)

#car1 = Car('Toyota', 'Corolla', 3000)

car2 = Car('Toyota', 'Corova', int(input('Please input the year of production')))
# raises Exception('Эта машина еще не была выпущена')
