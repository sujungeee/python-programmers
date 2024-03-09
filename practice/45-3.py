# 참고 코드

from collections import deque
def solution(board):
    def bfs(start):
        direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}  # 북,동,남,서 순서
        length = len(board)
        visited = [[float('inf')] * length for _ in range(length)]
        visited[0][0] = 0

        q = deque([start])  # x, y, cost, dir
        while q:
            x, y, cost, d = q.popleft()
            for i in range(4):  # 북,동,남,서 순서
                nx = x + direction[i][0]
                ny = y + direction[i][1]

                # board 안에 있고, 벽이 아닌지 확인
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    if i == d:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])

        return visited[-1][-1]

    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))