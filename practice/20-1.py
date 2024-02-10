# 효율성 테스트 실패: count 함수가 안에 들어가서 O(n*n) 이 돼서 실패함 .. . 딕셔너리 다시 만들었더니 해결
# 교재 답안도 거의 비슷하니
# 20-2는 교재 참고 코드 대신 프로그래머스 다른 사람 풀이 참고 코드

def solution(participant, completion):
    answer= ''

    par1= {}

    for par in participant:
        if par in par1:
            par1[par]+= 1
        else:
            par1[par]= 1

    for fin in completion:
        par1[fin] -= 1
        if par1[fin] == 0:
            del par1[fin]

    par1=list(par1)[0]
    return answer.join(par1)



print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))