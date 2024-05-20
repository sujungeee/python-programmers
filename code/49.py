# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 유망 함수
# 1. 남은 피로도가 최소 필요 피로도보다 같거나 높아야 한다.
# 2. 한 번 방문했던 던전은 재방문이 안된다.


def solution(k, dungeons):
    visited= [False] * len(dungeons)
    def backtracking(k, num, visited): # k: 남은 피로도
        result= num
        for idx, dungeon in enumerate(dungeons):
            if k>= dungeon[0] and visited[idx]==False:
                visited[idx]= True
                result= max(result, backtracking(k-dungeon[1], num+1, visited))
                visited[idx]= False

        return result

    maxNum= backtracking(k, 0, visited)
    return maxNum

print(solution(80, [[80,20], [50,40], [30,10]]))
