# LCS 길이 구하기
# 공통된 부분은 최대한 유지하고
# 추가 공통된 부분은 그 동안 공통 부분의 +1
def solution(str1, str2):
    m= len(str1)
    n= len(str2)

    dp= [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

print(solution('ABCBDAB', 'BDCAB'))
print(solution('AGGTAB', 'GXTXAYB'))