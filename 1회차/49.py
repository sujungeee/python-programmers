# 최소 필요 피로도
# 소모 피로도
def backtrack(k, cnt, dungeons, visited):
    result= cnt
    for idx, dungeon in enumerate(dungeons):
        if dungeon[0] <= k and visited[idx] == False:
            visited[idx]= True
            result= max(result, backtrack(k-dungeon[1], cnt+1, dungeons, visited))
            visited[idx]= False
    return result

def solution(k, dungeons):
    visited= [False] * len(dungeons)
    maxnum= backtrack(k, 0, dungeons, visited)

    return maxnum

print(solution(80, [[80,20], [50,40], [30,10]]))