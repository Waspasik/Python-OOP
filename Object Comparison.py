# Класс Vector
# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс
# должен принимать два аргумента в следующем порядке:

# x — координата вектора по оси x
# y — координата вектора по оси y

# Экземпляр класса Vector должен иметь следующее формальное строковое представление:

# Vector(<координата x>, <координата y>)

# Также экземпляры класса Vector должны поддерживать операции сравнения с помощью операторов
# == и!=. Два вектора считаются равными, если их координаты по обеим осям совпадают. Методы,
# реализующие операции сравнения, должны уметь сравнивать как два вектора между собой, так
# и вектор с кортежем из двух чисел, представляющих координаты x и y.

# Примечание 1. Числами будем считать экземпляры классов int и float.

# Примечание 2. Если объект, с которым выполняется операция сравнения, некорректен, метод,
# реализующий эту операцию, должен вернуть константу NotImplemented.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.x, self.y) == other
        elif isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented



# Класс Word
# Будем называть словом любую последовательность из одной или более латинских букв.

# Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один
# аргумент:

# word — слово

# Экземпляр класса Word должен иметь следующее формальное строковое представление:

# Word('<слово в исходном виде>')

# И следующее неформальное строковое представление:

# <слово, в котором первая буква заглавная, а все остальные строчные>

# Также экземпляры класса Word должны поддерживать между собой все операции сравнения с помощью
# операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины совпадают. Слово
# считается больше другого слова, если его длина больше.

# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод,
# реализующий эту операцию, должен вернуть константу NotImplemented.

from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word):
        self.word = word
    
    def __str__(self):
        return self.word.title()
    
    def __repr__(self):
        return f"Word('{self.word}')"
    
    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented



# Класс Month
# Реализуйте класс Month, описывающий месяц. При создании экземпляра класс должен принимать два
# аргумента в следующем порядке:

# year — год
# month — порядковый номер месяца

# Экземпляр класса Month должен иметь следующее формальное строковое представление:

# Month(<год>, <порядковый номер месяца>)

# И следующее неформальное строковое представление:

# <год>-<порядковый номер месяца>

# Также экземпляры класса Month должны поддерживать все операции сравнения с помощью операторов
# ==, !=, >, <, >=, <=. Два Month объекта считаются равными, если их годы и порядковые номера
# месяцев совпадают. Month объект считается больше другого Month объекта, если его год больше.
# В случае если два Month объекта имеют равные года, большим считается тот, чей месяц больше.
# Методы, реализующие операции сравнения, должны уметь сравнивать как два Month объекта между
# собой, так и Month объект с кортежем из двух чисел, представляющих год и месяц.

# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод,
# реализующий эту операцию, должен вернуть константу NotImplemented.

from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month
    
    def __str__(self):
        return f"{self.year}-{self.month}"
    
    def __repr__(self):
        return f"Month({self.year}, {self.month})"
    
    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.year, self.month) == other
        elif isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, tuple):
            return (self.year, self.month) > other
        elif isinstance(other, Month):
            return (self.year, self.month) > (other.year, other.month)
        return NotImplemented



# Класс Version
# Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра
# класс должен принимать один аргумент:

# version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например,
# 2.8.1. Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна
# версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0

# Экземпляр класса Version должен иметь следующее формальное строковое представление:

# Version('<версия ПО в виде трех целых чисел, разделенных точками>')

# И следующее неформальное строковое представление:

# <версия ПО в виде трех целых чисел, разделенных точками>

# Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью
# операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными, если все три числа в их
# версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в
# его версии больше. Или если второе число в его версии больше, если первые числа совпадают. Или
# если третье число в его версии больше, если первые и вторые числа совпадают.

# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий
# эту операцию, должен вернуть константу NotImplemented.

from functools import total_ordering
from re import fullmatch


@total_ordering
class Version:
    def __init__(self, version):
        if fullmatch(r'\d+', version):
            self.version = version + '.0.0'
        elif fullmatch(r'\d+.\d+', version):
            self.version = version + '.0'
        else:
            self.version = version
    
    def __str__(self):
        return self.version
    
    def __repr__(self):
        return f"Version('{self.version}')"
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version.split('.'))) == list(map(int, other.version.split('.')))
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version.split('.'))) > list(map(int, other.version.split('.')))
        return NotImplemented
