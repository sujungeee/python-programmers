def solution(N, stages):
    fails={}
    total= len(stages)

    challengers= [0]*(N+2)
    for stage in stages:
        challengers[stage] +=1 # 현 스테이지에 머물러있는 사람의 수를 저장, 인덱스는 스테이지를 의미(N+2, 0~N, N+1 까지)

    for i in range(1, N+1):
        if challengers[i] == 0:
            fails[i]=0
        else:
            fails[i]= challengers[i]/total
            total-= challengers[i]
    result= sorted(fails, key=lambda x: fails[x], reverse=True)

    return result

print(solution(4, [4,4,4,4,4]))