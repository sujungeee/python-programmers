def solution(k, dungeons):
    ans= []
    visited= [False for _ in range(len(dungeons))]
    def bt(values, cnt, visited):
        ans.append(cnt)

        for idx, dungeon in enumerate(dungeons):
            if visited[idx] == False and values >= dungeon[0]:
                visited[idx]= True
                bt(values-dungeon[1], cnt+1, visited)
                visited[idx]= False


    bt(k, 0, visited)
    return max(ans)

print(solution(80, [[80,20],[50,40],[30,10]]))


# def backtrack(k, cnt, dungeons, visited):
#     result= cnt
#     for idx, dungeon in enumerate(dungeons):
#         if dungeon[0] <= k and visited[idx] == False:
#             visited[idx]= True
#             result= max(result, backtrack(k-dungeon[1], cnt+1, dungeons, visited))
#             visited[idx]= False
#     return result
#
# def solution(k, dungeons):
#     visited= [False] * len(dungeons)
#     maxnum= backtrack(k, 0, dungeons, visited)
#
#     return maxnum