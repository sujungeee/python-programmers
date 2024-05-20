def solution(record):
    answer= []
    uidName={}

    for r in record:
        command=r.split()

        if command[0] in ['Enter', 'Change']:
            uidName[command[1]]= command[2]

    for r in record:
        command= r.split()
        uid= command[1]
        if command[0] == 'Enter':
            answer.append(uidName[uid] + "님이 들어왔습니다.")
        elif command[0] == 'Leave':
            answer.append(uidName[uid] + "님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))