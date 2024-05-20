# 교재 참고 코드
import math
from collections import deque

def solution(progresses, speeds):
    answer= []
    length= len(progresses)
    endDate= deque([0]*length)
    for i in range(length):
        endDate[i]= int(math.ceil((100-progresses[i])/speeds[i]))

    count= 0
    function1= endDate[0]
    for i in range(length):
        if endDate[i] <= function1:
            count+=1
        else:
            answer.append(count)
            count= 1
            function1= endDate[i]

    answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))