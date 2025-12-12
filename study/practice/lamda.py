# lamda

add = lambda x, y: x + y
print(add(3, 5))

# sorted에서 key로 활용
words = ["apple", "banana", "kiwi", "strawberry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# map과 filter 조합
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
print(squared, even)
