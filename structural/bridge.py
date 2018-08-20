# -*- coding: utf8 -*-

"""
Имя: Мост (Bridge)

Тип: Структурный.

Суть: Разделяет абстракцию и релализацию так,
что бы они могли изменяться не зависимо.
"""


# abstract tv
class TVBase(object):
    def tune_channel(self, channel):
        raise NotImplementedError


class SonyTV(TVBase):
    def tune_channel(self, channel):
        print('Sony TV: канал сейчас: {!s}'.format(channel))


class PhilipsTV(TVBase):
    def tune_channel(self, channel):
        print('Philips TV: канал сейчас: {!s}'.format(channel))


# abstract RemoteControl
class RemoteControlBase(object):
    def __init__(self):
        self.tv = self.get_tv()

    def get_tv(self):
        raise NotImplementedError

    def tune_channel(self, channel):
        self.tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0

    def get_tv(self):
        return SonyTV()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


def main():
    remote_control = RemoteControl()
    remote_control.tune_channel(5)
    remote_control.next_channel()
    remote_control.next_channel()
    remote_control.tv = PhilipsTV()
    remote_control.next_channel()
    remote_control.previous_channel()


if __name__ == '__main__':
    main()
