# 내가 짠 코드
def hashValue(query):
    p = 31
    m = 1_000_000_007
    n=0
    hashValue= 0
    for s in query:
        hashValue += (ord(s)-96)*(p**n)
        n+= 1
        hashValue= hashValue % m

    return hashValue


def solution(string_list, query_list):
    answer= ['False']*(len(query_list))

    dict1 = {}

    for query in query_list:
        dict1[hashValue(query)]= query

    for string in string_list:
        if hashValue(string) in dict1:
           answer[query_list.index(string)]= 'True'

    return answer

print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))