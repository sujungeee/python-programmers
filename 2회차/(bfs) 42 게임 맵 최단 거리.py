from collections import deque
def solution(maps):
    m= len(maps)
    n= len(maps[0])
    directions= [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동, 서, 남, 북
    visited= [[False for _ in range(n)] for _ in range(m)]
    visited[0][0]= True

    def bfs(sx, sy, dx, dy):
        que = deque()
        que.append([sx, sy, 1])

        while que:
            x, y, cnt= que.popleft()
            if x==dx and y==dy:
                return cnt

            for dir in directions:
                newx, newy= x+dir[0], y+dir[1]
                if 0<=newx<m and 0<=newy<n and maps[newx][newy]==1:
                    if not visited[newx][newy]:
                        visited[newx][newy]= True
                        que.append([newx, newy, cnt+1])

        return -1

    return bfs(0, 0, m-1, n-1)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))