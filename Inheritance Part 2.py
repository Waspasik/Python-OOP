# Классы BasicPlan и подклассы
# 1. Реализуйте класс BasicPlan, описывающий подписку базового уровня на некотором онлайн-сервисе.
# При создании экземпляра класс не должен принимать никаких аргументов.

# Класс BasicPlan должен иметь семь атрибутов:

# can_stream —  атрибут, имеющий значение True
# can_download — атрибут, имеющий значение True
# has_SD — атрибут, имеющий значение True
# has_HD — атрибут, имеющий значение False
#  has_UHD — атрибут, имеющий значение False
# num_of_devices — атрибут, имеющий значение 1
# price — атрибут, имеющий значение 8.99$

# 2. Также реализуйте класс SilverPlan, наследника класса BasicPlan, описывающий подписку среднего
# уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса SilverPlan должен совпадать
# с процессом создания экземпляра класса BasicPlan.

# Класс SilverPlan должен иметь семь атрибутов:

# can_stream —  атрибут, имеющий значение True
# can_download — атрибут, имеющий значение True
# has_SD — атрибут, имеющий значение True
# has_HD — атрибут, имеющий значение True
#  has_UHD — атрибут, имеющий значение False
# num_of_devices — атрибут, имеющий значение 2
# price — атрибут, имеющий значение 12.99$

# 3. Наконец, реализуйте класс GoldPlan, наследника класса BasicPlan, описывающий подписку высокого
# уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса GoldPlan должен совпадать
# с процессом создания экземпляра класса BasicPlan.

# Класс GoldPlan должен иметь семь атрибутов:

# can_stream —  атрибут, имеющий значение True
# can_download — атрибут, имеющий значение True
# has_SD — атрибут, имеющий значение True
# has_HD — атрибут, имеющий значение True
#  has_UHD — атрибут, имеющий значение True
# num_of_devices — атрибут, имеющий значение 4
# price — атрибут, имеющий значение 15.99$

class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'


class SilverPlan(BasicPlan):
    has_UHD = False
    num_of_devices = 2
    price = '12.99$'


class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'



# Классы WeatherWarning и WeatherWarningWithDate
# Реализуйте класс WeatherWarning, описывающий объект, предупреждающий о погодных изменениях. При
# создании экземпляра класс не должен принимать никаких аргументов.

# Класс WeatherWarning должен иметь три метода экземпляра:

# rain() — метод, выводящий текст:

# Ожидаются сильные дожди и ливни с грозой

# snow() — метод, выводящий текст:

# Ожидается снег и усиление ветра

# low_temperature() — метод, выводящий текст:

# Ожидается сильное понижение температуры

# Также реализуйте класс WeatherWarningWithDate, наследника класса WeatherWarning, описывающий объект,
# предупреждающий о погодных изменениях с указанием даты. Процесс создания экземпляра класса
# WeatherWarningWithDate должен совпадать с процессом создания экземпляра класса WeatherWarning.

# Класс WeatherWarningWithDate должен иметь три метода экземпляра:

# rain() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:

# <дата в формате DD.MM.YYYY>
# Ожидаются сильные дожди и ливни с грозой

# snow() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:

# <дата в формате DD.MM.YYYY>
# Ожидается снег и усиление ветра

# low_temperature() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:

# <дата в формате DD.MM.YYYY>
# Ожидается сильное понижение температуры

# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что
# реализованный класс используется только с корректными данными.

class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')
    
    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date):
        print(date.strftime('%d.%m.%Y'))
        super().rain()
    
    def snow(self, date):
        print(date.strftime('%d.%m.%Y'))
        super().snow()
    
    def low_temperature(self, date):
        print(date.strftime('%d.%m.%Y'))
        super().low_temperature()



# Классы Triangle и EquilateralTriangle
# Реализуйте класс Triangle, описывающий треугольник. При создании экземпляра класс должен принимать
# три аргумента в следующем порядке:

# a — длина стороны треугольника
# b — длина стороны треугольника
# c — длина стороны треугольника

# Класс Triangle должен иметь один метод экземпляра:

# perimeter() — метод, возвращающий периметр треугольника

# Также реализуйте класс EquilateralTriangle, наследника класса Triangle, описывающий равносторонний
# треугольник. При создании экземпляра класс должен принимать один аргумент:

# side — длина стороны треугольника

# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что
# реализованный класс используется только с корректными данными.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return sum((self.a, self.b, self.c))
    

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)



# Класс Counter и DoubledCounter
# Вам доступен класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс принимает
# один аргумент:

# start — начальное значение счетчика, по умолчанию равняется 0

# Экземпляр класса Counter имеет один атрибут:

# value — текущее значение счетчика

# Класс Counter имеет два метода экземпляра:

# inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.

# Если число не передано, метод увеличивает значение счетчика на единицу

# dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число.
# Если число не передано, метод уменьшает значение счетчика на единицу. Значение счетчика считается равным 0
# если при уменьшении оно становится отрицательным

# Реализуйте класс DoubledCounter, наследника класса Counter, описывающий неотрицательный счетчик, значение
# которого увеличивается и уменьшается дважды при вызове соответствующих методов. Процесс создания экземпляра
# класса DoubledCounter должен совпадать с процессом создания экземпляра класса Counter.

# Экземпляр класса DoubledCounter должен иметь один атрибут:

# value — текущее значение счетчика

# Класс DoubledCounter должен иметь два метода экземпляра:

# inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число
# дважды. Если число не передано, метод должен увеличить значение счетчика на два

# dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число
# дважды. Если число не передано, метод должен уменьшить значение счетчика на два. Значение счетчика считается
# равным 0, если при уменьшении оно становится отрицательным

# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный
# класс используется только с корректными данными.

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)

        
class DoubledCounter(Counter):
    def inc(self, n=1):
        super().inc(n*2)
          
    def dec(self, n=1):
        super().dec(n*2)



# Классы Summator и подклассы🌶️
# 1. Реализуйте класс Summator, описывающий объект, вычисляющий сумму натуральных чисел от 1 до n:

# 1 + 2 + 3 + ... + n

# При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Summator должен иметь один метод экземпляра:

# total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел от 1 до n
# включительно

# 2. Помимо этого, реализуйте класс SquareSummator, наследника класса Summator, описывающий объект, вычисляющий
# сумму квадратов натуральных чисел от 1 до n:
# 1^2 + 2^2 + 3^2 + ... + n^2
 
# Процесс создания экземпляра класса SquareSummator должен совпадать с процессом создания экземпляра класса
# Summator.

# Класс SquareSummator должен иметь один метод экземпляра:

# total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму квадратов целых чисел
# от 1 до n включительно

# 3. Также реализуйте класс QubeSummator, наследника класса Summator, описывающий объект, вычисляющий сумму
# кубов натуральных чисел от 
# 1 до n:

# 1^3 + 2^3 + 3^3 + ... + n^3
 
# Процесс создания экземпляра класса QubeSummator должен совпадать с процессом создания экземпляра класса
# Summator.

# Класс QubeSummator должен иметь один метод экземпляра:

# total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму кубов целых чисел от
# 1 до n включительно

# 4. Наконец, реализуйте класс CustomSummator, наследника класса Summator, описывающий объект, вычисляющий
# сумму произвольных степеней натуральных чисел от 
# 1 до n:

# 1^m + 2^m + 3^m + ... + n^m

# При создании экземпляра класс должен принимать один аргумент:

# m — степень чисел в последовательности

# Класс CustomSummator должен иметь один метод экземпляра:

# total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел в степени
# m от 1 до n включительно

# Примечание 1. Попытайтесь реализовать классы таким образом, чтобы метод total() был определен лишь в классе
# Summator.

# Реализация с методом total() в каждом дочернем классе:
class Summator:
    def total(self, n, degree=1):
        return sum(map(lambda x: x**degree, range(1, n+1)))
    

class SquareSummator(Summator):
    def total(self, n):
        return super().total(n, 2)
    

class QubeSummator(Summator):
    def total(self, n):
        return super().total(n, 3)


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return super().total(n, self.m)


# Реализация с методом total() только в родительском классе:
class Summator:
    def __init__(self, m=1):
        self.m = m

    def total(self, n):
        return sum(map(lambda x: x**self.m, range(1, n+1)))
    

class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)
    

class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)


class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)
        
