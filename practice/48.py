def solution(board):
    # 0. 1,2,3 이 모두 충족돼야함
    def is_valid(num, row, col):
        return not (in_row(num, row) or in_column(num, col) or in_box(num, row, col))

    # 1. 행에 채우고자 하는 num이 있는지
    def in_row(num, row):
        return num in board[row]

    # 2. 열에 채우고자 하는 num이 있는지
    def in_column(num, col):
        return num in (board[i][col] for i in range(9))

    # 3. 3X3 칸 내에 num이 있는지
    def in_box(num, row, col):
        box_row= (row // 3) * 3
        box_col= (col // 3) * 3
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col+3):
                if num == board[i][j]:
                    return True
        return False

    # 스도쿠 내의 빈 포지션의 인덱스 찾기
    def find_empty_position():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i,j
        return None

    def find_solution():
        empty_pos = find_empty_position()

        if not empty_pos:
            return True

        row, col= empty_pos
        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num
                if find_solution():
                    return True
                board[row][col]= 0
        return False

    find_solution()
    return board

print(solution([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]))
print(solution([
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]))