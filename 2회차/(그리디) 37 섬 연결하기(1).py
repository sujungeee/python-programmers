from collections import deque
# by 크루스칼 알고리즘
def solution(n, costs):
    result= 0 # 가중치 합
    que= deque(sorted(costs, key= lambda x:x[2])) # 오름차순으로 정렬

    MST= []
    minInfo= que.popleft()
    MST.append(minInfo)
    result+= minInfo[2]

    CPR= [i for i in range(n)]
    CPR[minInfo[1]]= minInfo[0]

    while len(MST)<n-1:
        info= que.popleft()
        start, end, weight= info
        # 사이클을 형성하는지 확인
        while CPR[start] != start:
            start= CPR[start]
        while CPR[end] != end:
            end= CPR[end]
        if start != end:
            CPR[end]= start
            MST.append(info)
            result+= weight

    print('MST: ', MST)
    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))