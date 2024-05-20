# 참고 코드
# https://velog.io/@mang0206/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-python
# https://velog.io/@ggb05224/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-python

from collections import deque
def bfs(start, end, maps):
    cost= 0
    direction= [[0,-1],[0,1],[-1,0],[1,0]] # 좌우상하

    X = len(maps)
    Y = len(maps[0])

    # visited(방문했는지에 대한 배열)
    visited = [[False] * Y for _ in range(X)]
    q= deque()
    # 시작 지점
    for i in range(X):
        for j in range(Y):
            if maps[i][j] == start:
                sx, sy= i, j
                q.append([sx,sy,0])
                visited[sx][sy] = True

    while q:
        x, y, cost= q.popleft()

        if maps[x][y] == end:
            return cost

        for dir in direction:
            nx= x+dir[0]
            ny= y+dir[1]

            if 0<=nx<X and 0<=ny<Y and maps[nx][ny]!='X':
                if not visited[nx][ny]:
                    q.append([nx,ny,cost+1])
                    visited[nx][ny]= True
    return -1

def solution(maps):
    startToLever= bfs('S','L', maps)
    leverToExit= bfs('L','E', maps)

    if startToLever!= -1 and leverToExit!= -1:
        return startToLever+leverToExit

    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))