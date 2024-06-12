# https://school.programmers.co.kr/learn/courses/30/lessons/64065
from collections import Counter
def solution(s):
    result= []
    total= []
    s= s[2:-2].split('},{') # ['2', '2,1', '2,1,3', '2,1,3,4']
    for ss in s:
        sArray= ss.split(',') # ['2', '1', '3']
        for st in sArray:
            total.append(int(st))
    t1= Counter(total).most_common() # [(3, 4), (2, 3), (4, 2), (1, 1)]
    for t in t1:
        result.append(t[0])
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))