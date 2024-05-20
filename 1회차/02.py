def solution(arr):
    lst= list(set(arr))
    lst.sort(reverse=True)
    return lst

print(solution([1,3,3,4,2]))