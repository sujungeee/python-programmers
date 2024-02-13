# 내가 짠 코드
def solution(id_list, report, k):
    answer = []
    dic= {} # 키: 유저 ID, 값: 유저가 신고한 ID
    rpNumDic= {} # 키: 유저 ID, 값: 신고당한 횟수(중복 제외)


    for r in report:
        cmd= r.split(' ')
        if cmd[0] in dic:
            if cmd[1] in dic[cmd[0]]: # 아예 중복 신고 한 경우
                continue
            else:
                dic[cmd[0]].append(cmd[1])
        else:
            dic[cmd[0]]= [cmd[1]]

        rpNumDic[cmd[1]] = rpNumDic.get(cmd[1], 0) + 1

    for uid in id_list:
        cnt= 0
        if uid in dic:
            for i in dic[uid]:
                if rpNumDic[i]>= k:
                    cnt+= 1
                else:
                    continue
        else:
            cnt= 0
        answer.append(cnt)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))