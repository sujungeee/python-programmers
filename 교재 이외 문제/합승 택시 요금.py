def solution(n, s, a, b, fares):
    # 플로이드-워셜 알고리즘-> 각 노드에서 노드까지의 최단 거리
    costs = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        costs[i][i] = 0

    for fare in fares:
        costs[fare[0]][fare[1]] = fare[2]
        costs[fare[1]][fare[0]] = fare[2]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                costs[i][j] = min(costs[i][k] + costs[k][j], costs[i][j])

    # 각 노드(s)에서 a, b, s로 가기까지 최단 거리들을 구하기
    results= []
    for cost in costs:
        results.append(cost[a]+cost[b]+cost[s])

    return min(results)

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))