# 딕셔너리 + Counter(best)

import collections

def solution(want, number, discount):
    answer= 0
    dict1= dict(zip(want, number))

    for i in range(len(discount)-9):
        if dict1 == collections.Counter(discount[i:i+10]):
            answer+= 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))