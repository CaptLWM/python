'''
    예외 처리
    
    - except는 여러개 사용 가능
    - finally는 무조건 실행
'''
try:
    value = int(input("숫자 입력: "))
    print(10 / value)
except ValueError:
    print("숫자만 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
finally:
    print("프로그램 종료.")
