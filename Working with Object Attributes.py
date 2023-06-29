# Класс Item
# Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен
# был принимать три аргумента в следующем порядке:

# name — название предмета
# price — цена предмета в рублях
# quantity — количество предметов

# Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться
# его название с заглавной буквы, а при обращении к атрибуту total — произведение цены предмета
# на его количество.

# Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте
# правильный класс Item.

# before
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total': 
            return self.price * self.quantity
        elif name == 'name':
            return self.name.title()
        return self.__dict__[name]

# after
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr):
        if attr == 'name':
            return object.__getattribute__(self, attr).title()
        return object.__getattribute__(self, attr)
    
    def __getattr__(self, attr):
        if attr == 'total': 
            return self.price * self.quantity
        raise AttributeError



# Класс Logger
# Требовалось реализовать класс Logger. При создании экземпляра класс не должен был принимать
# никаких аргументов.

# Предполагалось, что при установке или изменении значения атрибута экземпляра класса Logger
# будет выводиться текст:

# Изменение значения атрибута <имя атрибута> на <новое значение атрибута>

# Также планировалось, что при удалении атрибута будет выводиться текст:

# Удаление атрибута <имя атрибута>

# Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте
# правильный класс Logger.

# before
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.name = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.name

# after
class Logger:
    def __setattr__(self, attr, value):
        print(f'Изменение значения атрибута {attr} на {value}')
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print(f'Удаление атрибута {attr}')
        del self.__dict__[attr]



# Класс Ord
# Реализуйте класс Ord. При создании экземпляра класс не должен принимать никаких аргументов.

# Экземпляр класса Ord должен выступать в качестве альтернативы функции ord(). При обращении к
# атрибуту экземпляра, именем которого является одиночный символ, должна возвращаться его позиция
# в таблице символов Unicode.

class Ord:
    def __getattr__(self, attr):
        if len(attr) == 1:
            return ord(attr)
        raise AttributeError



# Класс DefaultObject
# Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный
# аргумент default, имеющий значение по умолчанию None, а после произвольное количество именованных
# аргументов. Аргументы, передаваемые после default, должны устанавливаться создаваемому экземпляру
# в качестве атрибутов.

# При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение
# default.

class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)
    
    def __getattr__(self, attr):
        if attr not in self.__dict__:
            return self.default
        return self.__dict__[attr]



# Класс Const
# Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество
# именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру
# в качестве атрибутов.

# Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения, но
# не разрешать изменять значения этих атрибутов, а также удалять их. При попытке изменить значение
# атрибута должно возбуждаться исключение AttributeError с текстом:

# Изменение значения атрибута невозможно

# При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:

# Удаление атрибута невозможно

class Const:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)
    
    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        self.__dict__[attr] = value
    
    def __delattr__(self, attr):
        raise AttributeError('Удаление атрибута невозможно')
