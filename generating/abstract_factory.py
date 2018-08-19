# -*- coding: utf8 -*-
"""
Имя: Абстрактная фабрика (Abstracted Factory, KIT)

Тип: Порождающий объекты.

Суть: Предоставляет интерфейс для создания групп связанных или
зависимы объектов, не указывая их конкретный класс.

Замечание: Классы `Абстрактоной фабрики` часто реализуются
паттерном `Фабричный метод`, но могут быть реализованы и с
помощью паттерна `Прототип`.
"""


# abstract factory
class MenuDay(object):

    def create_breakfast(self):
        raise NotImplementedError

    def create_lunch(self):
        raise NotImplementedError

    def create_dinner(self):
        raise NotImplementedError


# object 1
class Breakfast(object):

    def __init__(self, food, drink):
        self._food = food
        self._drink = drink

    def __str__(self):
        return 'food: {!s}; drink: {!s}'.format(self._food, self._drink)


# object 2
class Lunch(object):

    def __init__(self, food, drink):
        self._food = food
        self._drink = drink

    def __str__(self):
        return 'food: {!s}; drink: {!s}'.format(self._food, self._drink)


# object 3
class Dinner(object):

    def __init__(self, food, drink):
        self._food = food
        self._drink = drink

    def __str__(self):
        return 'food: {!s}; drink: {!s}'.format(self._food, self._drink)


# concrete factory 1
class Monday(MenuDay):

    def create_breakfast(self):
        return Breakfast('toast', 'coffee')

    def create_lunch(self):
        return Lunch('soup', 'juice')

    def create_dinner(self):
        return Dinner('meat', 'tea')


# concrete factory 2
class Tuesday(MenuDay):

    def create_breakfast(self):
        return Breakfast('corn flakes', 'coffee')

    def create_lunch(self):
        return Lunch('salad and fish', 'juice')

    def create_dinner(self):
        return Dinner('steak and salad', 'tea')


# client
class Menu(object):

    @staticmethod
    def monday():
        return Monday()

    @staticmethod
    def tuesday():
        return Tuesday()


def main():
    menu = Menu().monday()
    print(menu.create_breakfast())
    print(menu.create_dinner())
    print(menu.create_lunch())


if __name__ == '__main__':
    main()
