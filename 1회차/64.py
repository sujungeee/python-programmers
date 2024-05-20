def solution(n):
    sarray= [[0]*n for _ in range(n)]
    num= 1

    start_row, end_row= 0, n-1
    start_col, end_col= 0, n-1

    while start_row<=end_row and start_col<=end_col:
        # 첫 번째 행 채우기
        for i in range(start_col, end_col+1):
            sarray[start_row][i]= num
            num+= 1
        start_row+= 1

        # 마지막 열 채우기
        for i in range(start_row, end_row+1):
            sarray[i][end_col]= num
            num+= 1
        end_col-= 1

        # 마지막 행 채우기
        for i in range(end_col, start_col-1, -1):
            sarray[end_row][i]= num
            num+= 1
        end_row-= 1

        # 첫 번재 열 채우기
        for i in range(end_row, start_row-1, -1):
            sarray[i][start_col]= num
            num+= 1
        start_col+= 1

    return sarray

print(solution(3))
print(solution(4))