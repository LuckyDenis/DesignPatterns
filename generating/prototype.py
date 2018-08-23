# -*- coding: utf8 -*-
"""
Имя: Прототип (Prototype)

Тип: Порождающий объекты.

Суть: Определяет несколько видов объектов, что бы при создании
использовать объекты-прототипы и создать новые объекты,
копирую прототип.
"""


import copy


class Prototype(object):
    def __init__(self):
        self._objects = dict()

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attr):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


class Food(object):
    """Еда"""


def main():
    prototype = Prototype()
    prototype.register('food', Food())
    tomato = prototype.clone('food', {'name': 'tomato'})
    print(type(tomato), tomato.name)
    orange = prototype.clone('food', {'name': 'orange'})
    print(type(orange), orange.name)


if __name__ == '__main__':
    main()
