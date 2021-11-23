# -*- coding: utf-8 -*-
# 과제: 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의
# 뒷자리를 * 문자로 변경하시오.
#
# 정규 표현식을 전혀 모르면 ...
# 1. 전체 텍스트를 공백 문자로 나눈다.(split)
# 2. 나누어진 단어들이 주민등록번호 형식인지 조사한다.
# 3. 단어가 주민등록번호 형식이라면 뒷자리를 '*'로 변환한다.
# 4. 나누어진 단어들을 다시 조립한다.
import re  # 정규 표현식을 사용하기 위한 re모듈
data = """
park 800905-1049118
kim 700905-1059119
"""
result = []  # ['park 800905-*******', 'kim 700905-*******']
for line in data.split("\n"):
    word_result = []  # ['park', '800905-*******']
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
'''
park 800905-*******
kim 700905-*******
'''
# 반면에 정규식을 사용하면 다음처럼 휠씬 간편하고 직관적인 코드를 작성할 수 있다.
data = """
park 800905-1049118
kim 700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))  # \g<그룹이름>을 참조한다. 즉 (\d{6})를 지칭한다.
'''
park 800905-*******
kim 700905-*******
'''
