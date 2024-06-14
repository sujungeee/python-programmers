# 내가 짠 코드
import itertools
def solution(numbers, target):
    cnt= 0
    sign= ['+', '-']
    arrays= list(itertools.product(sign, repeat= len(numbers)))

    for array in arrays:
        total= 0
        for idx, value in enumerate(array):
            if value=='+':
                total+=numbers[idx]
            else:
                total-= numbers[idx]
        if total == target:
            cnt+=1

    return cnt

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))