# 이중 우선순위 큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# /* 문제 */
# 이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다. 전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다. 이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다. 데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.
# 정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.
# Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.

# 1. 데이터를 삽입하는 연산: I 숫자
# 2. 데이터를 삭제하는 연산
#   2-1. 우선 순위가 가장 높은 것(최댓값)을 삭제: D 1
#   2-2. 우선 순위가 가장 낮은 것(최솟값)을 삭제: D -1

# 힙- 삭제 및 삽입 연산의 시간 복잡도: O(logN)

import heapq
def solution(operations):
    heap= []
    for op in operations:
        str, value= op.split()
        if str == 'I': # 삽입
            heapq.heappush(heap, int(value))
        elif op == 'D 1' and heap: # 최댓값 삭제
            heap.remove(max(heap))
        elif op == 'D -1' and heap: # 최솟값 삭제
            heapq.heappop(heap)

    if heap == []:
        return [0,0]
    else:
        return [max(heap), heap[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))