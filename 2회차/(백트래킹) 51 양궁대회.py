from collections import Counter
from itertools import combinations_with_replacement
def solution(n, info):
    result= []
    global diff
    diff= 0

    def cpScore(com): # 점수 비교
        global diff
        score1= 0 # 어피치 점수
        score2= 0 # 라이언 점수
        rionScore= []

        for i in range(11):
            rionScore.append(com[10-i])
            if info[i] == 0 and com[10-i] == 0:
                continue
            if info[i] < com[10-i]:
                score2= score2 + (10-i)
            else:
                score1= score1 + (10-i)

        if score2 - score1 > 0 and score2 - score1 > diff:
            diff= score2-score1
            result.clear()
            result.append(rionScore)
        elif score2 - score1 > 0 and score2 - score1 == diff:
            result.append(rionScore)

    for coms in combinations_with_replacement(range(11), n):
        com= Counter(coms)
        cpScore(com)

    if len(result)>=1:
        return result[0]
    else:
        return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))