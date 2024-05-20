# 교재 + 내가 짜기
def solution(triangle):
    n= len(triangle)
    dp= triangle.copy()

    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[i][j]= dp[i][j] + max(dp[i+1][j], dp[i+1][j+1])

    return dp[0][0]

print(solution([[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]))