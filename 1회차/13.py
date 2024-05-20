def stackList(board): # Board 배열을 스택으로 구성하기
    N = len(board[0])
    stackList = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                stackList[j][N - 1 - i] = board[i][j]
            else:
                stackList[j].pop(N - 1 - i)
    return stackList
def solution(board, moves):
    answer=0
    stack= stackList(board)
    blanket=[]
    for i in moves:
        # 인형 넣기
        if stack[i-1]:
            new= stack[i-1].pop()
            blanket.append(new)
        if len(blanket)>=2 and blanket[-2]==new:
            blanket.pop()
            blanket.pop()
            answer+=2
    return answer