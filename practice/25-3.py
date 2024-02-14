# 프로그래머스 다른 사람 코드
# https://school.programmers.co.kr/learn/courses/30/lessons/72411/solution_groups?language=python3
# counter.most_common 사용

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer= []

    for num in course:
        menu = []

        for order in orders:
            menu += combinations(sorted(order),num)
        counter= Counter(menu)

        for key, value in counter.items():
            if (value >= 2) and (value == counter.most_common()[0][1]):
                answer.append("".join(key))

    return sorted(answer)

print(solution(["BACGF", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))