a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
else:
    print("Loop is done")
print(result)

b=[1,2,3,4]
result2 = [num * 3 for num in b]
print(result2)

c = ["apple", "banana", "cherry"]
for i, fruit in enumerate(c):
    print(f"{i}: {fruit}")

d = ["apple", "banana", "cherry"]
e = ["sweet", "yellow", "red"]
for fruit, color in zip(d, e):
    print(f"{fruit} is {color}")