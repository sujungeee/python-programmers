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
        # 연속으로 같은 인형이 들어온 경우, 단 blanket에 2개는 있어야 연속된 값을 삭제할 수 있다.
        if len(blanket)>=2 and blanket[-2]==new:
            blanket.pop()
            blanket.pop()
            answer+=2
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))