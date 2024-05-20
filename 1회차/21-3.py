# 교재 참고 코드: 딕셔너리끼리의 비교

def solution(want, number, discount):
    answer= 0
    dict1= dict(zip(want, number))

    for i in range(len(discount)-9):
        discount_10d= {}

        for j in range(i, i+10):
            if discount[j] in dict1:
                discount_10d[discount[j]]= discount_10d.get(discount[j], 0) +1

        if discount_10d == dict1:
            answer+= 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
print(solution(["apple"], [10],
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))