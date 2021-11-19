# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number%2==1: # 2로 나누었을 때 1이면 홀수이다.
        return True
    else:
        return False
print(is_odd(3))
# True
print(is_odd(4))
# False

# 2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(avg_numbers(1, 2))
# 1.5
print(avg_numbers(1,2,3,4,5))
# 3.0

# 3
def fib(n):
    if n==0 : return 0 # n이 0일 때는 0을 리턴
    if n==1 : return 1# n이 1일 때는 1을 리턴
    return fib(n-2)+fib(n-1)  # n이 2이상일 때는 그 이전의 두 값을 더하여 리턴 7 / 8
for i in range(10):
    print(fib(i), end=' ')
# 0 1 1 2 3 5 8 13 21 34