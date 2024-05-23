def solution(n, computers):
    visited= set()
    netNum= 0

    graph= {i: [] for i in range(1,n+1)}
    for idx1, com in enumerate(computers):
        for idx2, c in enumerate(com):
            if c == 1:
                graph[idx1+1].append(idx2+1)

    def dfs(node):
        visited.add(node)
        for nodes in graph[node]:
            if nodes == node:
                continue
            if nodes not in visited:
                dfs(nodes)

    while len(visited)<n:
        for i in range(1, n+1):
            if i not in visited:
                dfs(i)
                netNum+=1

    return netNum

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))