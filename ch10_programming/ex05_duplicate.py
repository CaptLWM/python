# -*- coding: utf-8 -*-
def duplicatedNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10


print(duplicatedNum("0123456789"))  # True 리턴
print(duplicatedNum("01234"))  # False 리턴
print(duplicatedNum("01234567890"))  # False 리턴
print(duplicatedNum("6789012345"))  # True 리턴
print(duplicatedNum("012322456789"))  # False 리턴
