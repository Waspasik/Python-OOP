# Класс Circle
# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать
# один аргумент:

# radius — радиус круга

# Экземпляр класса Circle должен иметь один атрибут:

# radius — радиус круга

# Класс Circle должен иметь один метод класса:

# from_diameter() — метод, принимающий в качестве а

class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)



# Класс Rectangle
# Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс
# должен принимать два аргумента в следующем порядке:

# length — длина прямоугольника
# width — ширина прямоугольника

# Экземпляр класса Rectangle должен иметь два атрибута:

# length — длина прямоугольника
# width — ширина прямоугольника

# Класс Rectangle должен иметь один метод класса:

# square() — метод, принимающий в качестве аргумента число side и возвращающий экземпляр
# класса Rectangle c длиной и шириной, равными side

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    @classmethod
    def square(cls, side):
        return cls(side, side)



# Класс QuadraticPolynomial
# Квадратный трехчлен – это многочлен вида ax^2 + bx + c, где a != 0. Например:

# x^2 + 1
# x^2 - 5x + 6

# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра
# класс должен принимать три аргумента в следующем порядке:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена

# Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена

# Класс QuadraticPolynomial должен иметь четыре свойства:

# Класс QuadraticPolynomial должен иметь два метода класса:

# from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов
# a, b и c, которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса
# QuadraticPolynomial, созданный на основе переданных коэффициентов

# from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты
# a, b и c квадратного трехчлена, записанные через пробел. Метод должен возвращать экземпляр класса
# QuadraticPolynomial, созданный на основе переданных коэффициентов, предварительно преобразованных
# в экземпляры класса float

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iter_obj):
        a, b, c = iter_obj
        return cls(a, b, c)
    
    @classmethod
    def from_str(cls, string):
        a, b, c = map(float, string.split())
        return cls(a, b, c)



# Класс StrExtension
# Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании
# экземпляра класс не должен принимать никаких аргументов.

# Класс StrExtension должен иметь три статических метода:

# remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные
# латинские буквы без учета регистра и возвращает полученный результат

# leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы,
# не являющиеся латинскими буквами, и возвращает полученный результат

# replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в
# строке string все символы из chars на char с учетом регистра и возвращает полученный результат.

# Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.

class StrExtension():
    @staticmethod
    def remove_vowels(string):
        vowels = 'aeiouy'
        return ''.join(list(filter(lambda x: x.lower() not in vowels, string)))
    
    @staticmethod
    def leave_alpha(string):
        alphabet = [chr(i) for i in range(65, 123) if chr(i).isalpha()]
        return ''.join(list(filter(lambda x: x in ''.join(alphabet), string)))
    
    @staticmethod
    def replace_all(string, chars, char):
        return ''.join([char if i in chars else i for i in string ])



# Класс CaseHelper 🌶️
# Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом
# нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой
# буквы. Например, bee_geek и hello_world.

# Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно
# без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

# Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case
# и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.

# Класс CaseHelper должен иметь четыре статических метода:

# is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная
# строка записана в стиле Snake Case, или False в противном случае

# is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если
# переданная строка записана в стиле Upper Camel Case, или False в противном случае

# to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case,
# записывает ее в стиле Snake Case и возвращает полученный результат

# to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case,
# записывает ее в стиле Upper Camel Case и возвращает полученный результат

import re


class CaseHelper:
    @staticmethod
    def is_snake(string):
        snake_pattern = r'^[a-z]+_*([a-z]+)+'
        if re.fullmatch(snake_pattern, string):
            return True
        return False
    
    @staticmethod
    def is_upper_camel(string):
        camel_pattern = r'^[A-Z][a-z]+([A-Z][a-z]+)*'
        if re.fullmatch(camel_pattern, string):
            return True
        return False
    
    @staticmethod
    def to_snake(string):
        result = string[0].lower() + ''.join([f'_{i.lower()}' if i.isupper() else i for i in string[1::]])
        return result

    @staticmethod
    def to_upper_camel(string):
        result = ''.join(list(map(lambda x: x.title(), string.split('_'))))
        return result
