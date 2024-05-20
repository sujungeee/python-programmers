# 프로그래머스 다른 사람 풀이
# https://school.programmers.co.kr/learn/courses/30/lessons/42885/solution_groups?language=python3
from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1

    return result

print(solution([70,50,80,50], 100))
print(solution([70,80,50], 100))