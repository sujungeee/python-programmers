# 아무것도 안보고 푼 나의 더러미 코드 (어지럽다)
import math
from collections import deque

def solution(progresses, speeds):
    answer= []
    length= len(progresses)
    endDate= deque([0]*length)
    for i in range(length):
        endDate[i]= int(math.ceil((100-progresses[i])/speeds[i]))
    function1= endDate.popleft()
    count= 1
    while len(endDate) != 0:
        if endDate[0] and function1 >= endDate[0]:
            count = count+ 1
            endDate.popleft()
            if len(endDate)==0:
                answer.append(count)
        elif endDate[0] and function1 < endDate[0]:
            answer.append(count)
            count= 1
            function1= endDate.popleft()
            if len(endDate)==0:
                answer.append(1)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))