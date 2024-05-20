# 교재 참고 코드
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
    result= []
    # string_list 에 대한 해시 함수의 결과를 hash_list에 저장
    hash_list= [hashValue(str) for str in string_list]

    for query in query_list:
        query_hashValue= hashValue(query)
        if query_hashValue in hash_list:
            result.append(True)
        else:
            result.append(False)

    return result


print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))