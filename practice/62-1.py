def solution(arr, n):
    arrLength = len(arr)
    rotArr= arr.copy() # arr의 복사본

    for _ in range(n):
        answer = [[0] * arrLength for _ in range(arrLength)]
        for i in range(arrLength):
            for j in range(arrLength):
                answer[j][arrLength-i-1]= rotArr[i][j]
        rotArr= answer
    return answer


print(solution([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
], 1))

print(solution([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
], 2))