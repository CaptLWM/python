# -*- coding:utf-8 -*-
# __str__메서드는 print(e) 처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print("허용되지 않는 별명입니다.")
    print(e)
'''
천사
허용되지 않는 별명입니다.
허용되지 않는 별명입니다.
'''
3
