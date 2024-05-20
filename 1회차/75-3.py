# solution by 그리디

def solution(triangle):
    # dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])

print(solution([[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]))