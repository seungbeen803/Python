# 합집합
from unittest import result


def union(*ar):
    result = [] # 빈 방
    for item in ar:
        for x in item:
            result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))