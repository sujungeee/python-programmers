# 프로그래머스 다른 사람 코드
# https://school.programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3
def solution(phone_book):
    dic= {}
    for phone_number in phone_book:
        dic[phone_number]= 1
    for phone_number in phone_book:
        tmp= ''
        for number in phone_number:
            tmp+= number # 폰 번호 한글자씩
            if tmp in dic and tmp!= phone_number:
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))