# -*- coding:utf-8 -*-
# 오류 일부러 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    pass


# class Eagle(Bird):
# def fly(self):
# print("very fast")
eagle = Eagle()
eagle.fly()
'''
Traceback (most recent call last):
    File "...", line 16, in <module>
        eagle.fly()
    File "...", line 6, in fly
        raise NotImplementedError
NotImplementedError
'''
