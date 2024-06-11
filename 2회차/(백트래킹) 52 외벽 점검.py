# 백트래킹에서 -> 재귀로 모든 경우의 수를 호출하고 재귀 호출 후 조건을 설정하였는데,
# 이번 문제는 순열로 모든 경우의 수를 생성하고, if-break를 통해 조건을 설정하였음.
from itertools import permutations
def solution(n, weak, dist):
    length= len(weak)

    for i in range(length):
        weak.append(weak[i]+n)
    answer= len(dist) + 1

    for start in range(length):
        for friends in permutations(dist, len(dist)):
            cnt= 1
            position= weak[start]+friends[cnt-1]
            for idx in range(start, start+length):
                if position < weak[idx]:
                    cnt+=1
                    if cnt > len(dist):
                        break
                    position= weak[idx] + friends[cnt-1]
            answer= min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))