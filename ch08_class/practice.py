class Calculator():
    def __init__(self, num):
        self.num = num

    def sum(self):
        result = 0
        for num in self.num:
            result += num
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.num)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
# 15
print(cal1.avg())
# 3.0
cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
# 40
print(cal2.avg())
# 8.0
