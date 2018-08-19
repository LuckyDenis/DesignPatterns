# -*- coding: utf8 -*-
"""
Имя: Одиночка (Singleton)

Тип: Порождающий объекты.

Суть: Гарантирует, что класс имеет только один экземпляр и
предоставляет глобальную точку доступа к нему.

Замечание: С помощью паттерна `Одиночка` часто реализуется
многие паттерны (`Абстрактная фабрика`, `Строитель`, `Прототип`)
"""


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        cls.get_instance = classmethod(lambda c: c._instance)
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    obj1 = Singleton('My object class 1')
    print(obj1.get_name())
    obj2 = Singleton('My object class 2')
    print(obj2.get_name())


if __name__ == '__main__':
    main()
