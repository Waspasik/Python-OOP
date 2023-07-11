# Иерархия классов 🛸
# С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих
# транспортные средства

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class Motocycle(LandVehicle):
    pass


class Bicycle(LandVehicle):
    pass


class Propeller(AirVehicle):
    pass


class Jet(AirVehicle):
    pass



# Иерархия классов 🔶
# С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих
# геометрические фигуры

class Shape:
    pass


class Polygon(Shape):
    pass


class Circle(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Triangle(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass



# Иерархия классов 🐍
# С помощью наследования и приведенной ниже схемы постройте иерархию классов, описывающих животных

# Класс Animal должен иметь два метода экземпляра:

# sleep() — пустой метод
# eat()— пустой метод

# Класс Fish должен иметь один метод экземпляра:

# swim()— пустой метод

# Класс Bird должен иметь один метод экземпляра:

# lay_eggs()— пустой метод

# Класс FlyingBird должен иметь один метод экземпляра:

# fly()— пустой метод

class Animal:
    def sleep(self):
        pass
    
    def eat(self):
        pass
    

class Fish(Animal):
    def swim(self):
        pass
    
    
class Bird(Animal):
    def lay_eggs(self):
        pass
    
    
class FlyingBird(Bird):
    def fly(self):
        pass



# Классы User и PremiumUser
# Реализуйте класс User, описывающий пользователя некоторого интернет-ресурса. При создании экземпляра
# класс должен принимать один аргумент:

# name — имя пользователя

# Класс User должен иметь один метод экземпляра:

# skip_ads() — метод, всегда возвращающий False 

# Также реализуйте класс PremiumUser, наследника класса User, описывающий пользователя некоторого
# интернет-ресурса с премиум подпиской. Процесс создания экземпляра класса PremiumUser должен совпадать
# с процессом создания экземпляра класса User.

# Класс PremiumUser должен иметь один метод экземпляра:

# skip_ads() — метод, всегда возвращающий True 

class User:
    def __init__(self, name):
        self.name = name
    
    def skip_ads(self):
        return False


class PremiumUser(User):
    def skip_ads(self):
        return True



# Классы Validator и NumberValidator
# Реализуйте класс Validator, описывающий объект, проверяющий значение на корректность. При создании
# экземпляра класс должен принимать один аргумент:

# obj — произвольный объект

# Класс Validator должен иметь один метод экземпляра:

# is_valid() — пустой метод, всегда возвращающий значение None

# Также реализуйте класс NumberValidator, наследника класса Validator, описывающий объект, проверяющий
# значение на принадлежность типу int или float. Процесс создания экземпляра класса NumberValidator должен
# совпадать с процессом создания экземпляра класса Validator.

# Класс NumberValidator должен иметь один метод экземпляра:

# is_valid() — метод, возвращающий True, если значение переданное в инициализатор принадлежит типу int
# или float, или False в противном случае

class Validator:
    def __init__(self, obj):
        self.obj = obj
    
    def is_valid(self):
        pass


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj, int | float)



# Класс Counter и подклассы
# 1. Реализуйте класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс должен
# принимать один аргумент:

# start — начальное значение счетчика, по умолчанию равняется 0

# Экземпляр класса Counter должен иметь один атрибут:

# value — текущее значение счетчика

# Класс Counter должен иметь два метода экземпляра:

# inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.

# Если число не передано, метод должен увеличить значение счетчика на единицу
# dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число.
# Если число не передано, метод должен уменьшить значение счетчика на единицу. Значение счетчика считается
# равным 0, если при уменьшении оно становится отрицательным

# 2. Также реализуйте класс NonDecCounter, наследника класса Counter, описывающий счетчик, значение которого
# можно увеличивать, но нельзя уменьшать. Процесс создания экземпляра класса NonDecCounter должен совпадать
# с процессом создания экземпляра класса Counter.

# Экземпляр класса NonDecCounter должен иметь один атрибут:

# value — текущее значение счетчика

# Класс NonDecCounter должен иметь один метод экземпляра:

# dec() — пустой метод. Сигнатура метода должна совпадать с сигнатурой метода dec() класса Counter

# 3. Наконец, реализуйте класс LimitedCounter, наследника класса Counter, описывающий счетчик, значение
# которого можно увеличивать лишь до определенного числа. При создании экземпляра класс должен принимать
# два аргумента в следующем порядке:

# start — начальное значение счетчика, по умолчанию равняется 0
# limit — максимально возможное значение счетчика, по умолчанию равняется 10

# Экземпляр класса LimitedCounter должен иметь один атрибут:

# value — текущее значение счетчика

# Класс LimitedCounter должен иметь один метод экземпляра:

# inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.

# Если число не передано, метод должен увеличить значение счетчика на единицу. При увеличении значения счетчика
# метод не должен превышать установленный лимит

class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, num=1):
        self.value += num

    
    def dec(self, num=1):
        self.value -= num
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def __init__(self, value):
        self.value = value

    def dec(self, num=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit
        self.value = self.start
    
    def inc(self, num=1):
        self.value += num
        if self.value > self.limit:
            self.value = self.limit
