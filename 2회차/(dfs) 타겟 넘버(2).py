# 프로그래머스 다른 사람 코드 참고
# 1) 재ㅐㅐ귀. 멋있는 코드.

def solution(numbers, target):
    if not numbers and target == 0:
        return 1 # 조건 충족 시 +1
    elif not numbers:
        return 0 # 조건 충족 X 이면 0 반환
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
        # 앞 solution 재귀: number를 뺐을 때
        # 뒤 solution 재귀: nubmer를 더했을 때


# 2) * 사용
# *: 리스트 안에 있는 튜플들을 튜플 별로 언패킹해줌.
# product(*l): 각 튜플들을 항으로 생각해서 튜플 안의 있는 값 중 하나를 항으로 선택하여,
# sum: 완성된 n개의 한 튜플을 더한 값들을 모두 s(list)에 저장.!

from itertools import product
def solution2(numbers, target):
    l= [(x, -x) for x in numbers]
    s= list(map(sum, product(*l))) # 모든 경우의 수를 더하고 뺀 결과 값의 리스트
    return s.count(target)

print(solution([1, 1, 1, 1, 1], 3))
print(solution2([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
print(solution2([4, 1, 2, 1], 4))