# 이렇게 해도 될 것 같은데,,
def solution(nums):
    cnt= 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            cnt+=1
    return cnt

# solution2:
def solution2(nums):
    dp= [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i]= max(dp[j]+1, dp[i])
    return max(dp)

print(solution([1, 4, 2, 3, 1, 5, 7, 3]))
print(solution2([1, 4, 2, 3, 1, 5, 7, 3]))
print(solution([3, 2, 1]))
print(solution2([3, 2, 1]))