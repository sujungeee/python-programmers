# sol2) 다른 사람 코드 참고
# bin: 정수를 이진수 "문자열" 로 돌려준다.
def solution(s):
    a, b= 0, 0
    while s != '1':
        a+= 1
        num= s.count('1')
        b+= len(s) - num
        s= bin(num)[2:]

    return [a, b]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
print(solution("1000"))


# sol1) 쌩구현
# def solution(s):
#     cnt0, cnt1= 0, 0 # cnt0: 이진 변환 횟수, cnt1: 제거된 0의 개수
#     def binary(cnt):
#         binaryStr= ""
#         remainder= []
#         while cnt > 0:
#             remainder.append(cnt % 2)
#             cnt= cnt//2
#         remainder.reverse()
#         for i in remainder:
#             binaryStr+= str(i)
#         return binaryStr
#
#     checkStr= s[:]
#     while checkStr != '1':
#         startNum = sum([1 for s in checkStr if s == '1']) # 1의 개수 구하기
#         binaryStr= binary(startNum) # 1을 이진수로 변환
#         cnt0 += 1 # 이진 변환 횟수 1 추가
#         cnt1 = cnt1 + len(checkStr)- startNum # 0의 개수 추가
#         checkStr= binaryStr
#
#     return [cnt0, cnt1]