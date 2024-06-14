# 딕셔너리의 키를 이용한 코드를 짜보았다.
# 밑의 코드가 더 가독성이 좋은듯.

def solution(n, computers):
    cnt= 0
    visited= set()

    # 모든 컴퓨터가 상호 연결되어 있으므로 굳이 두 번 graph append할 필요 X
    graph= {i: [] for i in range(n)}
    for idx1, computer in enumerate(computers):
        for idx2, com in enumerate(computer):
            if idx1 == idx2:
                continue
            if com == 1:
                graph[idx1].append(idx2)

    keyValue= list(graph.keys())

    while len(keyValue)>0:
        start = keyValue.pop()
        if start not in visited:
            visited.add(start)
            cango = []
            cango.extend(graph[start])
            del graph[start]
            while cango:
                node= cango.pop()
                if node not in visited:
                    visited.add(node)
                    cango.extend(graph[node])
            cnt+=1

    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))



# def solution(n, computers):
#     cnt= 0
#     visited= set()
#
#     graph= {i: [] for i in range(n)}
#     for idx1, computer in enumerate(computers):
#         for idx2, com in enumerate(computer):
#             if idx1 == idx2:
#                 continue
#             if com == 1:
#                 graph[idx1].append(idx2)
#
#     def dfs(node):
#         visited.add(node)
#         for nodes in graph[node]:
#             if nodes not in visited:
#                 dfs(nodes)
#
#     while len(visited)<n:
#         for i in range(n):
#             if i not in visited:
#                 dfs(i)
#                 cnt+=1
#
#     return cnt