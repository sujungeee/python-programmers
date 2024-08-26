def solution(k, m, score):
    result= 0
    scores= sorted(score)

    for i in range(len(score), 0, -m):
        tmp= scores[i-m:i]
        if tmp:
            result+= tmp[0]*m

    if len(score) < m:
        result= 0

    return result

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))