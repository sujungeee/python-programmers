def solution(numbers):
    arr= []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            arr.append(numbers[i] + numbers[j])
    arr= sorted(set(arr))
    return arr

print(solution([5,0,2,7]))