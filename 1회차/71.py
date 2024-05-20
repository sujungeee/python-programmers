# LIS 길이 구하기
# pseudo
# 각 i 에 대해서
# 0~i-1까지의 nums에서 nums[i]보다 작은 수가 나오면 기존 dp[i]에 +1
# 따라서 현 i 에 대해 nums[i] 의 값보다 작은 수들의 length들을 각각 구하고, 그 중에 가장 큰 dp가 최장 길이 부분 수열임

def solution(nums):
    dp= [1]*(len(nums))

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i]= max(dp[i],dp[j]+1)

    return max(dp)

print(solution([1,4,2,3,1,5,7,3]))
print(solution([3,2,1]))