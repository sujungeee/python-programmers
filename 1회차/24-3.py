# 프로그래머스 다른 사람 코드
# https://school.programmers.co.kr/learn/courses/30/lessons/92334/solution_groups?language=python3
# set 활용
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k: # 신고 대상자
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))