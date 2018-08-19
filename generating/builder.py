# -*- coding: utf8 -*-
"""
Имя: Строитель (Builder)

Тип: Порождающий объекты.

Суть: Разделяет создания сложного объекта и инцилизацию
его состояние так, что одинаковый процесс построения может
создать объекты с разными состояниям.
От абстрактной фабрики отличается тем, что делате акцент на
пошаговом констрировании объекта. Строитель возвращает объект
на последнем шаге, тогда как `Абстрактная фабртика` возвращает
объект немедленно.

Замечание: `Строитлеь` часто используется для создания паттерна
`Компоновщик`.
"""


# abstract builder
class Builder(object):

    def build_name(self):
        raise NotImplementedError

    def build_bun(self):
        raise NotImplementedError

    def build_cutlet(self):
        raise NotImplementedError

    def build_sauce(self):
        raise NotImplementedError

    def build_vegetables(self):
        raise NotImplementedError

    def build_burger(self):
        raise NotImplementedError


# product
class Burger(object):

    def __init__(self, name, bun, cutlet, sauce, vegetables):
        self._name = name
        self._bun = bun
        self._cutlet = cutlet
        self._sauce = sauce
        self._vegetables = vegetables

    def __str__(self):
        compound = ('\tbun: {!s}\n'
                    '\tcutlet: {!s}\n'
                    '\tsauce: {!s}\n'
                    '\tvegetables: {!s}'.format(self._bun, self._cutlet,
                                                self._sauce, self._vegetables))
        return 'Burger name:\n\t{!s}\nCompound:\n{!s}\n'.format(self._name, compound)


class Name(object):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Bun(object):

    def __init__(self, bun):
        self._bun = bun

    def __str__(self):
        return self._bun


class Cutlet(object):

    def __init__(self, cutlet):
        self._cutlet = cutlet

    def __str__(self):
        return self._cutlet


class Sauce(object):

    def __init__(self, sauce):
        self._sauce = sauce

    def __str__(self):
        return self._sauce


class Vegetables(object):

    def __init__(self, vegetables):
        self._vegetables = vegetables

    def __str__(self):
        return self._vegetables


# Concreted Builder 1
class HamburgerBuilder(Builder):

    def build_name(self):
        return Name('Hamburger')

    def build_bun(self):
        return Bun('Bun with sesame seeds')

    def build_cutlet(self):
        return Cutlet('Pork cutlet')

    def build_sauce(self):
        return Sauce('Tomato sauce')

    def build_vegetables(self):
        return Vegetables('Lettuce, tomato, onion, greens')

    def build_burger(self):
        name = self.build_name()
        bun = self.build_bun()
        cutlet = self.build_cutlet()
        sauce = self.build_sauce()
        vegetables = self.build_vegetables()
        return Burger(name, bun, cutlet, sauce, vegetables)


# Concreted Builder 2
class ChickenBurgerBuilder(Builder):

    def build_name(self):
        return Name('ChickenBurger')

    def build_bun(self):
        return Bun('Bun with sesame seeds')

    def build_cutlet(self):
        return Cutlet('Chicken cutlet')

    def build_sauce(self):
        return Sauce('Tomato sauce')

    def build_vegetables(self):
        return Vegetables('Lettuce, tomato, greens')

    def build_burger(self):
        name = self.build_name()
        bun = self.build_bun()
        cutlet = self.build_cutlet()
        sauce = self.build_sauce()
        vegetables = self.build_vegetables()
        return Burger(name, bun, cutlet, sauce, vegetables)


# director
class Director(object):

    @staticmethod
    def build_hamburger():
        return HamburgerBuilder().build_burger()

    @staticmethod
    def build_chicken_burger():
        return ChickenBurgerBuilder().build_burger()


def main():
    builder = Director()
    burger = builder.build_hamburger()
    print(burger)
    burger = builder.build_chicken_burger()
    print(burger)


if __name__ == '__main__':
    main()
