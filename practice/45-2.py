# 참고 코드(2)
# https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EA%B2%BD%EC%A3%BC%EB%A1%9C-%EA%B1%B4%EC%84%A4-Python
from heapq import heappop, heappush

def solution(board):
    N= len(board)
    costBoard= [[[float('inf')]* N for _ in range(N)] for _ in range(4)]
    for i in range(4):
        costBoard[i][0][0]= 0

    heap= [(0,0,0,0), (0,0,0,2)] # 이동 비용, 출발 지점(x,y), 현재 방향

    while heap:
        cost, x, y, d= heappop(heap)

        for dx, dy, dd in ((1,0,0), (-1,0,1), (0,1,2), (0,-1,3)):
            nx, ny= x+dx, y+dy

            # 이동 좌표가 1. 벽 2. 좌표 밖 이면 pass
            if nx<0 or nx>=N or ny<0 or ny>=N or board[ny][nx]:
                continue

            newCost= cost+ (100 if d==dd else 600)

            if costBoard[dd][ny][nx]>newCost:
                costBoard[dd][ny][nx]= newCost
                heappush(heap, (newCost, nx, ny, dd))

    return min(costBoard[0][N-1][N-1], costBoard[1][N-1][N-1], costBoard[2][N-1][N-1], costBoard[3][N-1][N-1])


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))