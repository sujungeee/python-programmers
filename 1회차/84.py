from collections import Counter
def solution(k, tangerine):
    counter= Counter(tangerine)
    sorted_counts= sorted(counter.values(), reverse= True)
    count= 0
    typeIdx= 0

    for type in sorted_counts:
        count+= type
        typeIdx+= 1
        if count>=k:
            break

    return typeIdx

print(solution(6, [1,3,2,5,4,5,2,3]))
print(solution(4, [1,3,2,5,4,5,2,3]))
print(solution(2, [1,1,1,1,2,2,2,3]))
