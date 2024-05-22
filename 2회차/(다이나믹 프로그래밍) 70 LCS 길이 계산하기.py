def solution(str1, str2):
    m= len(str1)
    n= len(str2)
    dp= [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]: # 두 비교 값 같으면
                dp[i][j]= dp[i-1][j-1]+1 # 전까지의 최장 수열 길이 + 1
            else: # 두 비교 값이 다르면
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

print(solution('ABCBDAB', 'BDCAB'))
print(solution('AGGTAB', 'GXTXAYB'))