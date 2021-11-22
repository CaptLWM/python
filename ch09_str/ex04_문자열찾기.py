str_f = "Python code."
print("찾는 문자열의 위치:", str_f.find("Python"))
print("찾는 문자열의 위치:", str_f.find("code"))
print("찾는 문자열의 위치:", str_f.find("easy"))

str_f_se = "Python is powerful. Python is easy to learn"
print(str_f_se.find("Python", 10, 30))
print(str_f_se.find("Python", 35))

print("Python으로 시작?", str_f_se.startswith("Python"))
# Python으로 시작? True
print("is로 시작?", str_f_se.startswith('is'))
# is로 시작? False
