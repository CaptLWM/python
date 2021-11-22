print('Python'.isalpha())  # 문자열이 숫자, 특수문자, 공백이 아닌 경우 -> True
# True

print('Ver. 3.x'.isalpha())
# False

print('12345'.isdigit())
# True
print('12345abcx'.isdigit())
# False(문자 있기때문)

print('      '.isspace())
# True
print('123   '.isspace())
# False

print('PYTHON'.isupper())
# True
print('python'.isupper())
# False

# 대소문자로 변경하기
string1 = 'Python is powerful. PYTHON IS EASY TO LEARN.'
print(string1.lower())
print(string1.upper())
'''
python is powerful. python is easy to learn.
PYTHON IS POWERFUL. PYTHON IS EASY TO LEARN.
'''
