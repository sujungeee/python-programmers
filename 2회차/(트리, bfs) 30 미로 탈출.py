from collections import deque
def solution(maps):
    n= len(maps)
    m= len(maps[0])
    directions= [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동, 서, 남, 북

    for idx1, map in enumerate(maps):
        if 'S' in map:
            idx2= map.index('S')
            start= [idx1, idx2]
        if 'L' in map:
            idx2= map.index('L')
            lever= [idx1, idx2]
        if 'E' in map:
            idx2 = map.index('E')
            end = [idx1, idx2]

    def bfs(start, end):
        visited= [[False for _ in range(m)] for _ in range(n)]
        startX, startY= start
        endX, endY= end
        que= deque([[startX, startY, 0]])
        visited[startX][startY]= True

        while que:
            x, y, cost= que.popleft()
            if x == endX and y == endY:
                return cost

            for dir in directions:
                newx, newy= x+dir[0], y+dir[1]

                if 0<= newx<n and 0<=newy<m and maps[newx][newy]!='X':
                    if visited[newx][newy]==False:
                        visited[newx][newy]= True
                        que.append([newx, newy, cost+1])

        return -1

    # start-lever의 최단 거리 + lever-end의 최단 거리(단, 둘 중 하나라도 도달 못하면 -1 return)
    cost1= bfs(start, lever)
    cost2= bfs(lever, end)
    if cost1==-1 or cost2==-1:
        return -1
    return cost1+cost2

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))