def solution(nums):
    answer= 0
    pNum= len(set(nums)) # 폰켓몬 종류
    n2= int(len(nums)/2) # n/2
    # if pNum >= n2:
    #     answer= n2
    # else:
    #     answer= pNum
    return min(pNum,n2)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))