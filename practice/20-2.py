# 프로그래머스 다른 사람 풀이 참고 코드
import collections

def solution(participant, completion):
    answer= collections.Counter(participant)-collections.Counter(completion)
    answer= list(answer)[0]
    return answer

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))