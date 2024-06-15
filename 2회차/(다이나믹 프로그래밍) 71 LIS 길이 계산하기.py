def solution(nums):
    dp= [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i]= max(dp[j]+1, dp[i])
    return max(dp)

print(solution([1, 4, 2, 3, 1, 5, 7, 3]))
print(solution([3, 2, 1]))