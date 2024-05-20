from collections import deque
# 30번 문제랑 비슷
def solution(maps):
    # 상대 진영에 도달할 수 있으면 최단 거리 return
    # 맵의 크기 n*m 구하기
    m= len(maps)
    n= len(maps[0])
    visited=[[False]*n for _ in range(m)] # 좌표 방문 여부
    queue= deque()
    queue.append([1,1,1])
    visited[0][0]= True
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북

    while queue: # 탐색할 노드가 있으면
        x, y, distance= queue.popleft()
        # x, y가 n, m 이면(상대 진영에 도달하면 break)
        if x==m and y==n:
            return distance
        for move in direction:
            newx = move[0] + x
            newy = move[1] + y
            # 이동한게 범위 내면 append (n*m)
            if 1<=newx<=m and 1<=newy<=n and maps[newx-1][newy-1]!=0:
                    if not visited[newx-1][newy-1]:
                        queue.append([newx,newy,distance+1])
                        visited[newx-1][newy-1]= True

    return -1 # 상대 진영에 도달할 수 없으면 -1 return(상대 진영이 벽으로 가로 막혀있는 경우)

print(solution([[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,1], [0,0,0,0,1], [1,1,1,1,1]]))
print(solution([[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,0], [0,0,0,0,1]]))
