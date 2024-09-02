# 입국심사
# 1. 우선순위 큐: 시간 초과 남. .
import heapq


def solution1(n, times):
    result = 0
    que = [(time, idx) for idx, time in enumerate(times)]
    heapq.heapify(que)

    for i in range(n):
        value, idx = heapq.heappop(que)
        if i == n - 1:
            result = value
        heapq.heappush(que, (value + times[idx], idx))

    return result


# 2. 이진탐색
def solution2(n, times):
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2

        people = 0  # mid에 people 명이 입국심사 가능
        # start~mid
        for time in times:
            people += mid // time

        if people < n:  # 시간이 부족
            start = mid + 1
        else:
            end = mid - 1

    return start


# print(solution1(6, [7, 10]))
print(solution2(6, [7, 10]))