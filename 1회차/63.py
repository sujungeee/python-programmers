# 내가 짠 것
# 교재는
# 1. matrix 곱셈 연산
# 2. 전치 행렬 연산
# 나눴음. 실제로 문제를 풀 때는 기능을 1, 2로 나눠서 하는 것이 좋을 듯함
def solution(matrix1, matrix2):
    # max1 * max2 -> 전치
    arr= [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            value= 0
            for k in range(3):
                value+= matrix1[i][k]*matrix2[k][j] # 행렬의 곱셈
            arr[j][i]= value # 전치 행렬
    return arr

print(solution([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [9,8,7],
        [6,5,4],
        [3,2,1]
    ]
))

print(solution([
        [2,4,6],
        [1,3,5],
        [7,8,9]
    ],
    [
        [9,1,2],
        [4,5,6],
        [7,3,8]
    ]
))