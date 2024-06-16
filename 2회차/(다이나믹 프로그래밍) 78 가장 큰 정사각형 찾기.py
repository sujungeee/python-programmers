def solution(board):
    n= len(board)
    m= len(board[0])
    arr= [[0 for _ in range(m)] for _ in range(n)]
    arr[0]= board[0] # 첫 행 채우기
    # 첫 열 채우기
    for idx, b in enumerate(board):
        arr[idx][0]= b[0]

    for i in range(1, n):
        for j in range(1, m):
            left, up, diag= arr[i][j-1], arr[i-1][j], arr[i-1][j-1]
            if board[i][j] == 1:
                if left==up==diag:
                    arr[i][j]= left+1
                else:
                    arr[i][j]= min(left, up, diag)+1
            else:
                arr[i][j]= 0

    maxEdge= max(max(arr[i]) for i in range(len(arr)))
    return maxEdge**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))