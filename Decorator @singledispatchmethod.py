# Класс Processor
# Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

# Класс Processor имеет один статический метод:

# process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его
# в зависимости от его типа и возвращает полученный результат. Если тип переданного объекта не
# поддерживается методом, возбуждается исключение TypeError с текстом:

# Аргумент переданного типа не поддерживается

# Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod,
# чтобы он выполнял ту же задачу.

from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @process.register(int)
    @process.register(float)
    @staticmethod
    def intfloat_process(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def str_process(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def list_process(data):
        return sorted(data)
    
    @process.register(tuple)
    @staticmethod
    def tuple_process(data):
        return tuple(sorted(data))
    
    

# Класс Negator
# Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Negator должен иметь один статический метод:

# neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение.

# Если методу передается целое или вещественное число, он должен возвращать это число, взятое с
# противоположным знаком. Если методу в качестве аргумента передается булево значение, он должен
# возвращать булево значение, противоположное переданному. Если переданный объект принадлежит
# какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

# Аргумент переданного типа не поддерживается

from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def intfloat_neg(data):
        return data * -1
    
    @neg.register(bool)
    @staticmethod
    def bool_neg(data):
        return bool(data - 1)



# Класс Formatter
# Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Formatter должен иметь один статический метод:

# format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и
# выводящий информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект
# принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

# Аргумент переданного типа не поддерживается

# Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

# Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы
# коллекций.

from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    @format.register(float)
    @staticmethod
    def intfloat_format(data):
        print(f"Целое число: {data}" if isinstance(data, int) else f"Вещественное число: {data}")
    
    @format.register(list)
    @format.register(tuple)
    @staticmethod
    def listtuple_format(data):
        _type = 'списка' if isinstance(data, list) else 'кортежа'
        print(f"Элементы {_type}: {', '.join(map(str, data))}")
    
    @format.register(dict)
    @staticmethod
    def dict_format(data):
        print(f"Пары словаря: {', '.join(map(str, data.items()))}")



# Класс BirthInfo 🌶️
# Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс
# должен принимать один аргумент:

# birth_date — дата рождения, представленная в одном из следующих вариантов:

# экземпляр класса date
# строка с датой в ISO формате
# список или кортеж из трех целых чисел: года, месяца и дня

# Если дата рождения является некорректной или представлена в каком-либо другом формате, должно
# быть возбуждено исключение TypeError с текстом:

# Аргумент переданного типа не поддерживается
# Экземпляр класса BirthInfo должен иметь один атрибут:

# birth_date — дата рождения в виде экземпляра класса date

# Класс BirthInfo должен иметь одно свойство:

# age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть
# количество полных лет, прошедших с даты рождения на сегодняшний день

# Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то
# есть в день рождения его возраст увеличивается на один год.

from functools import singledispatchmethod
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
    
    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, birth_date):
        self.birth_date = datetime.strptime('-'.join(map(str, birth_date)), '%Y-%m-%d').date()

    @property
    def age(self):
        today = datetime.now()
        return relativedelta(today, self.birth_date).years
