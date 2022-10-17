# 05. random 모듈의 sample 함수를 사용하여 로또번호를 뽑는 프로그램을 작성하시오.

import random

def lotto():
    result = random.sample(range(1, 45), 6)
    result.sort()
    return result

print(lotto())