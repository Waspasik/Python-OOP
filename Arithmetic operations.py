# Класс FoodInfo
# Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра
# класс должен принимать три аргумента в следующем порядке:

# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах

# Экземпляр класса FoodInfoдолжен иметь три атрибута:

# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах

# И следующее формальное строковое представление:

# FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)

# Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью
# оператора +, результатом которой должен являться новый экземпляр класса FoodInfo с суммарным
# количеством белков, жиров и углеводов исходных экземпляров.

# Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления
# нацело на число n с помощью операторов *, / и // соответственно:

# результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров
# и углеводов которого умножены на n
# результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и
# углеводов которого поделены на n
# результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков,
# жиров и углеводов которого поделены нацело на n

# Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать,
# что экземпляр класса FoodInfo всегда делится на ненулевое число.

# Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод,
# реализующий эту операцию, должен вернуть константу NotImplemented.

class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        
    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"
    
    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                self.proteins * n,
                self.fats * n,
                self.carbohydrates * n
            )
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                self.proteins / n,
                self.fats / n,
                self.carbohydrates / n
            )
        return NotImplemented
    
    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                self.proteins // n,
                self.fats // n,
                self.carbohydrates // n
            )
        return NotImplemented



# Класс Vector
# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:

# x — координата вектора по оси x
# y — координата вектора по оси y

# Экземпляр класса Vector должен иметь следующее формальное строковое представление:

# Vector(<координата x>, <координата y>)

# Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания с
# помощью операторов + и - соответственно:

# результатом сложения должен являться новый экземпляр класса Vector, координата по оси x которого
# равна сумме координат по оси x исходных векторов, координата по оси y — сумме координат по оси y
# исходных векторов
# результатом вычитания должен являться новый экземпляр класса Vector координата по оси x которого
# равна разности координат по оси x исходных векторов с учетом порядка, координата по оси y —
# разности координат по оси y исходных векторов с учетом порядка

# Наконец, экземпляр класса Vector должен поддерживать операции умножения и деления на число n с
# помощью операторов * и / соответственно:

# результатом умножения должен являться новый экземпляр класса Vector, координаты которого умножены
# на n
# результатом деления должен являться новый экземпляр класса Vector, координаты которого поделены
# на n

# Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть
# возможность умножить как вектор на число, так и число на вектор.

# Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать,
# что экземпляр класса Vector всегда делится на ненулевое число.

# Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод,
# реализующий эту операцию, должен вернуть константу NotImplemented.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return Vector(*tuple(map(lambda x: x * n, (self.x, self.y))))
        return NotImplemented
    
    def __rmul__(self, n):
        if isinstance(n, (int, float)):
            return self.__mul__(n)
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return Vector(*tuple(map(lambda x: x / n, (self.x, self.y))))
        return NotImplemented



# Класс SuperString
# Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать
# один аргумент:

# string — значение строки

# Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:

# <значение строки>

# Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения
# с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString,
# представляющий конкатенацию исходных.

# Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового
# сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >>
# соответственно:

# результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную
# строку, умноженную на n;
# результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из
# первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n;
# результатом побитового сдвига влево должен являться новый экземпляр класса SuperString,
# представляющий исходную строку без последних n символов. Если n больше или равно длине исходной
# строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку;
# результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString,
# представляющий исходную строку без первых n символов. Если n больше или равно длине исходной
# строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку.

# Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть
# возможность умножить как строку на число, так и число на строку.

# Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое
# число.

# Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод,
# реализующий эту операцию, должен вернуть константу NotImplemented.

class SuperString:
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        return self.string
    
    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int):
            return SuperString(self.string * n)
        return NotImplemented
    
    def __rmul__(self, n):
        if isinstance(n, int):
            return self.__mul__(n)
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, int):
            return SuperString(self.string[:len(self.string) // n])
        return NotImplemented
    
    def __lshift__(self, n):
        if isinstance(n, int):
            if n == 0:
                return self
            return SuperString(self.string[:-n or None])
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if n == 0:
                return self
            return SuperString(self.string[n:])
        return NotImplemented
