# 프로그래머스 다른 사람 풀이 참고
# permutations(순열) 이용

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for order in permutations(range(n)):
        #print(t)
        cur = k
        local_ans = 0
        for t in order:
            require, consum = dungeons[t]
            if cur >= require:
                cur -= consum
                local_ans += 1
        answer = max(answer, local_ans)

    return answer

print(solution(80, [[80,20], [50,40], [30,10]]))