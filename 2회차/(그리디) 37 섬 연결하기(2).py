import heapq
# by 프림 알고리즘 using 우선순위 큐
def solution(n, costs):
    result= 0 # 가중치 합
    MST= []
    hq= []

    start= costs[0][0] # 임의의 노드 선택
    for cost in costs:
        if cost[0] == start:
            heapq.heappush(hq, [cost[2], cost[1]])
        elif cost[1] == start:
            heapq.heappush(hq, [cost[2], cost[0]])

    visited= set()
    visited.add(start)

    while len(visited) < n: # 노드를 기준으로
        weight, node= heapq.heappop(hq)

        if node not in visited:
            visited.add(node)
            MST.append([start, node, weight])
            start= node
            result+= weight

            for c in costs:
                if c[0] == node:
                    heapq.heappush(hq, [c[2], c[1]])
                elif c[1] == node:
                    heapq.heappush(hq, [c[2], c[0]])

    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))