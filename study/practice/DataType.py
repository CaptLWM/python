from collections import deque
from collections import defaultdict
from collections import Counter
import heapq

'''
    list [1,2,3,4]
    
    특징
        - 순서 있음(Ordered)
        - 변경 가능(Mutable)
        - 중복 허용
        - 인덱스 접근 가능

    시간 복잡도
        - 인덱스 접근 : O(1)
        - 끝에 append : O(1)
        - 중간 삽입/삭제: O(n)

    언제 사용?
        - 순서가 중요할 때
    
'''
squares = [n*n for n in range(1,6)]

print(squares)
# => [1, 4, 9, 16, 25]

'''
    tuple (10, 20, 30)

    특징
        - 순서 있음
        - 변경 불가능(Immuatable)
        - 리스트보다 안전하고 빠름
        - 딕셔너리의 key로 사용 가능

    언제 사용?
        - 수정되지 말아야 하는 데이터
        - 좌표, 설정값, 고정된 구조
'''
t = (10, 20, 30) # 튜플

'''
    dict {key:value, key:value}

    특징
        - key-value 구조
        - 순서 있음(Python 3.7+)
        - key 중복 불가
        - key는 immutable 타입만 가능(tuple, str 등)
            - tuple이 key로 쓰이는 대표적인 경우가 좌표를 사용할 때임
            - grid[(10,5)]="player" / 10,5 위치에 player
        - 조회 속도 빠름(해시 기반)

    시간 복잡도
        - key 조회/삽입/삭제 : O(1) 평균

    언제 사용?
        - 구조화된 데이터
        - 빠른 검색 필요할 때
        - JSON 같은 형태 데이터 처리
'''

user = {"name":"lee", "age" : 25}
print(user["name"])
user["age"]=26
print(user["age"])

'''
    set(집합) {1,2,3}

    특징
    
        - 순서 없음
        - 중복 없음
        - 해시 기반
        - 교집합/합집합 같은 집합 연산에 강함

    언제 사용?
        - 중복 제거
        - 빠른 포함 여부 체크
        - 집합 연산 필요할 때
    
'''

s = {1,2,3}
s.add(4)

a = {1, 2, 3}
b = {3, 4, 5}

print("교집합",a & b)  # 교집합
print("합집합",a | b)  # 합집합
print("차집합",a - b)  # 차집합

'''
    deque (collections.deque)

    특징
        - 양쪽 끝에서 빠른 삽입/삭제
        - queue나 stack 용도로 최적화
        - 리스트보다 빠름

    시간 복잡도
        - 양쪽 삽입/삭제 : O(1)
        - 중간 접근 : O(n)
'''

dq = deque([1,2,3])
print("deque0",dq)
dq.appendleft(0)
print("deque1",dq)
dq.append(4)
print("deque2",dq)

'''
    defaultdict / counter

    defaultdict
        - key가 없어도 기본값 자동 생성

    counter
         -값의 빈도 계산에 최적
'''
d = defaultdict(int)
print(d) #defaultdict(<class 'int'>, {})
d["a"] += 1
print(d) #defaultdict(<class 'int'>, {'a': 1})
cnt = Counter(["a","b","a"])
print(cnt) #Counter({'a': 2, 'b': 1})

'''
    heapq(최소 힙)

    특징
        - 우선순위 큐 구현
        - 항상 "가장 작은 값" 빠르게 꺼냄
'''

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
print(heapq.heappop(h))  # 1

'''
    참고) enumerate
        - 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용
        - 인덱스 번호와 컬렉션 원소를 tuple 형태로 반환
        
'''

et = [1,5,77,39,52]
for p in enumerate(et):
    print('enumerate',p)
'''
    enumerate (0, 1)
    enumerate (1, 5)
    enumerate (2, 77)
    enumerate (3, 39)
    enumerate (4, 52)
'''
for i, v in enumerate(et):
    print("index : {}, value: {}".format(i,v))
'''
    index : 0, value: 1
    index : 1, value: 5
    index : 2, value: 77
    index : 3, value: 39
    index : 4, value: 52
'''
