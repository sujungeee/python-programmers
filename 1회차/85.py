def solution(N, stations, W):
    answer= 0
    cnt= 1
    idx= 0

    while cnt<=N:
        if idx<len(stations) and cnt >= stations[idx]-W:
            cnt= stations[idx]+W+1
            idx+= 1
        else:
            cnt+= 2*W +1
            answer+=1

    return answer

print(solution(11, [4,11], 1))
print(solution(16, [9], 2))