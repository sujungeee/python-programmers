# 교재: 틀린 답......ㅋ 기각!!

def solution(board):

    def is_valid(x,y):
        return 0<=x<N and 0<=y<N

    def is_blocked(x,y): # 이동 불가능하면 true
        return (x,y) == (0,0) or not is_valid(x,y) or board[x][y]==1

    def calculate_cost(direction, prev_direction, cost):
        if prev_direction == -1 or (prev_direction-direction)%2==0: # 직선 거리
            return cost + 100
        else: # 코너
            return cost + 600

    def isSouldUpdate(x, y, direction, new_cost):
        return visited[x][y][direction]==0 or visited[x][y][direction]>new_cost

    queue=[(0,0,-1,0)]
    N= len(board)
    directions= [(0,-1),(0,1),(1,0),(-1,0)]
    visited= [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    answer= float('inf')

    while queue:
        x, y, prev_direction, cost= queue.pop(0)

        for direction, (dx,dy) in enumerate(directions):
            new_x= x+dx
            new_y= y+dy

            if is_blocked(new_x, new_y):
                continue

            new_cost= calculate_cost(direction, prev_direction, cost)

            if (new_x, new_y) == (N-1, N-1):
                answer= min(answer, new_cost)
            elif isSouldUpdate(new_x, new_y, direction, new_cost):
                queue.append((new_x, new_y, direction, new_cost))
                visited[new_x][new_y][direction]= new_cost

    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))