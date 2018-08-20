# -*- coding: utf8 -*-

"""
Имя: Компоновщик (Composite)

Тип: Структурный.

Суть: Компануюет объекты в древовидную структуру,
представляя их в виде иерархии. Позволяет клинту обращаться
как отдельному объекту, так и к целому поддереву.
"""


class Graphic(object):
    def draw(self):
        raise NotImplementedError

    def add(self, obj):
        raise NotImplementedError

    def remove(self, obj):
        raise NotImplementedError

    def get_child(self, index):
        raise NotImplementedError


class Line(Graphic):
    def draw(self):
        print('Line')


class Text(Graphic):
    def draw(self):
        print('Text')


class Brush(Graphic):
    def draw(self):
        print('Brush')


class Picture(Graphic):
    def __init__(self):
        self._children = list()

    def draw(self):
        for obj in self._children:
            obj.draw()

    def add(self, obj):
        if isinstance(obj, Graphic) and obj is not self._children:
            self._children.append(obj)

    def remove(self, obj):
        if isinstance(obj, Graphic) and obj is self._children:
            self._children.remove(obj)

    def get_child(self, index):
        return self._children[index]


def main():
    pic = Picture()
    pic.add(Text())
    pic.add(Line())
    pic.draw()
    line = pic.get_child(1)
    line.draw()


if __name__ == '__main__':
    main()
