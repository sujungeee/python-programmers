# 교재 코드
# 뭔가 굉장히 비효율적인 것 같다
def solution(id_list, report, k):
    answer= []
    dic= {}
    count= {}

    for r in report:
        uid, rid= r.split()
        if rid not in dic:
            dic[rid]= set()
        dic[rid].add(uid)

    for rid, uid_list in dic.items():
        if len(uid_list)>= k:
            for uid in uid_list:
                if uid not in count:
                    count[uid]= 1
                else:
                    count[uid]+= 1

    for i in range(len(id_list)):
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))