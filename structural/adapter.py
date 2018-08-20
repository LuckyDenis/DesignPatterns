# -*- coding: utf8 -*-

"""
Имя: Адаптер (Adapter)

Тип: Структурный.

Суть: Конвертирует интерфейс класса в другой интерфейс,
ожадиаеммый клиентом. Позволяет классам с разными
интерфейсами работать вместе.

"""


# first class
class Dog(object):
    def __init__(self, name):
        self._name = name

    def bark(self):
        return '{!s} говорит: `гав-гав`'.format(self._name)


# second class
class Cat(object):
    def __init__(self, name):
        self._name = name

    def meow(self):
        return '{!s} говорит: `мяу-мяу`'.format(self._name)


# adapter
class CatAdapter(Dog):
    def __init__(self, name):
        super(CatAdapter, self).__init__(name=name)
        self._cat = Cat(name=name)

    def bark(self):
        return self._cat.meow()


def main():
    dog = Dog('Бобик')
    print(dog.bark())
    dog = CatAdapter('Бобик')
    print(dog.bark())


if __name__ == '__main__':
    main()
