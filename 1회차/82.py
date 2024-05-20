
def solution(d, budget):
    count= 0
    d.sort()

    for e in d:
        if e > budget:
            break
        budget-= e
        count+= 1

    return count

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))