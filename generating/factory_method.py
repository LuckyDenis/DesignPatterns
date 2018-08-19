# -*- coding: utf8 -*-
"""
Имя: Фабричный метод (Factory Method)

Тип: Порождающий объекты.

Суть: Определяет интерфейс для создания объекта,
но позволяет подклассам, решать, какой класс инстанцировать.
Позволяет  делегировать создание объектов подклассам.

Замечание: `Абстрактная фабрика` часто реализуется
с помощью `Фабричный методов`.
`Фабричный метод` часто вызывается внутри шаблонный методов.
"""


# product
class Document(object):
    def show(self):
        raise NotImplementedError


class PDFDocument(Document):
    def show(self):
        return 'This is PDF document.'


class EPUBDocument(Document):
    def show(self):
        return 'This is EPUB document.'


class FB2Document(Document):
    def show(self):
        return 'This is FB2 document.'


# create / factory method
class App(object):
    def create_document(self, type_):
        raise NotImplementedError


# concrete create
class MyApp(App):
    def create_document(self, type_):
        if type_ is 'pdf':
            return PDFDocument()
        elif type_ is 'epub':
            return EPUBDocument()
        elif type_ is 'fb2':
            return FB2Document()


def main():
    app = MyApp()
    print(app.create_document('pdf').show())
    print(app.create_document('epub').show())
    print(app.create_document('fb2').show())


if __name__ == '__main__':
    main()