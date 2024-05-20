# 딕셔너리 + 덱: 같은 것을 빼고 empty한지 검사

from collections import deque


def solution(want, number, discount):
    answer = 0
    discount = deque(discount)
    for i in range(len(discount) - 9):
        dict1 = dict(zip(want, number))
        for j in range(10):
            if discount[j] in dict1:
                dict1[discount[j]] -= 1
                if dict1[discount[j]] == 0:
                    del dict1[discount[j]]
            else:
                continue
        if not dict1:
            answer += 1
        discount.popleft()

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
print(solution(["apple"], [10],
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))