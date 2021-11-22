# 필요없는 문자열 삭제
# str.strip([chars])
# 사이 문자는 삭제 불가

print("aaaapythonaaaa".strip('a'))
# python

test_str = "aaaaabbbpythonaaa"
temp1 = test_str.strip('b')
temp2 = temp1.strip('b')
print(temp1)

print(test_str.strip('ba'))

test_str_multi = "##****!!!!....python is powerful.!./..$%!!.@"
print(test_str_multi.strip('*#$! @./%'))

coffee_menu = "에스프레소, 아메리카노, 카페라떼, 카푸치노"
coffee_menu_list = coffee_menu.split(",")
print(coffee_menu_list)

coffee_list = []
for coffee in coffee_menu_list:
    temp = coffee.strip()
    coffee_list.append(temp)

print(coffee_list)
