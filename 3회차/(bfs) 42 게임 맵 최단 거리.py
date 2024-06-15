from collections import deque
def solution(maps):
    n= len(maps) # 행
    m= len(maps[0]) # 열
    directions= [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동, 서, 남, 북

    visited= [[False for _ in range(m)] for _ in range(n)]
    visited[0][0]= True

    que = deque([[0, 0, 1]])
    while que:
        x, y, cost = que.popleft()

        if x==n-1 and y==m-1:
            return cost

        for dir in directions:
            newx= x+dir[0]
            newy= y+dir[1]

            if 0<=newx<n and 0<=newy<m and maps[newx][newy]==1:
                if visited[newx][newy]==False:
                    visited[newx][newy]= True
                    que.append([newx, newy, cost+1])

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))