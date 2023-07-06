# Класс Point
# Реализуйте класс Point, описывающий точку в пространстве. При создании экземпляра класс должен
# принимать три аргумента в следующем порядке:

# x — координата точки по оси x
# y — координата точки по оси y
# z — координата точки по оси z

# Экземпляр класса Point должен иметь следующее формальное строковое представление:

# Point(<координата x>, <координата y>, <координата z>)

# Также экземпляр класса Point должен быть итерируемым объектом, элементами которого являются его
# координаты по осям x, y и z.

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._iter_obj = x, y, z
    
    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"
    
    def __iter__(self):
        yield from self._iter_obj



# Класс DevelopmentTeam
# Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший)
# и senior (старший). При создании экземпляра класс не должен принимать никаких аргументов.

# Класс DevelopmentTeam должен иметь два метода экземпляра:

# add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых
# является именем разработчика, и добавляющий их в число junior-разработчиков
# add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых
# является именем разработчика, и добавляющий их в число senior-разработчиков

# Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются
# все его junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть
# представлены в виде кортежей:

# (<имя разработчика>, 'junior')

# в то время как senior-разработчики — в виде кортежей:

# (<имя разработчика>, 'senior')

# Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.

class DevelopmentTeam:
    def __init__(self):
        self._junior = []
        self._senior = []

    def add_junior(self, *args):
        for dev in map(lambda x: (x, 'junior'), args):
            self._junior.append(dev)

    def add_senior(self, *args):
        for dev in map(lambda x: (x, 'senior'), args):
            self._senior.append(dev)
    
    def __iter__(self):
        yield from self._junior + self._senior



# Класс SkipIterator
# Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в
# следующем порядке:

# iterable — итерируемый объект
# n — целое неотрицательное число

# Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого
# объекта iterable, пропуская по n элементов, а затем возбуждает исключение StopIteration.

# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что
# реализованный класс используется только с корректными данными.

# Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы
# __iter__() и __next__(). Реализация же протокола может быть произвольной.

class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self._index = -n-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self._index += self.n+1
        if self._index >= len(self.iterable):
            raise StopIteration
        else:
            return self.iterable[self._index]



# Класс RandomLooper
# Реализуйте класс RandomLooper. При создании экземпляра класс должен принимать произвольное
# количество позиционных аргументов, каждый из которых является итерируемым объектом.

# Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке
# все элементы всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение
# StopIteration.

# Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их
# порядком в тестовых данных.

# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что
# реализованный класс используется только с корректными данными.

# Примечание 3. Класс RandomLooper должен удовлетворять протоколу итератора, то есть иметь методы
# __iter__() и __next__(). Реализация же протокола может быть произвольной.

from random import shuffle

class RandomLooper:
    def __init__(self, *args):
        self.iterables = args
        self.flatten_iterables = [item for iterable in self.iterables for item in iterable]
        shuffle(self.flatten_iterables)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.flatten_iterables):
            item = self.flatten_iterables[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
