from collections import defaultdict
import heapq
def solution(n, costs):
    visited= set()
    start= costs[0][0] # 0번 노드먼저 시작

    graph= defaultdict(list)
    for cost in costs:
        graph[cost[0]].append([cost[2], cost[1]])
        graph[cost[1]].append([cost[2], cost[0]])

    que = []
    heapq.heappush(que, [0, start])
    result= 0

    while que:
        d, node= heapq.heappop(que)
        if node not in visited:
            visited.add(node)
            result+=d

        if len(visited) == n:
            break

        for weight, adj in graph[node]:
            if adj not in visited:
                heapq.heappush(que, [weight, adj])

    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))