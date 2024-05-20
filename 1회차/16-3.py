# 프로그래머스 다른 사람 풀이 참고
from collections import deque
def solution(progresses, speeds):
    answer= []
    progresses= deque(progresses)
    speeds= deque(speeds)
    time= 0
    count= 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0])>=100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            if count>0:
                answer.append(count)
                count= 0
            time += 1
    answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))