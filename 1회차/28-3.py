# 프로그래머스 다른 사람 코드
# https://school.programmers.co.kr/learn/courses/30/lessons/12985/solution_groups?language=python3
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

print(solution(8, 4, 7))