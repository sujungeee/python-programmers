# 1. 그래프로 DFS를 진행(스택 이용)
def dfs(computers, visited, node): # 집합
    stack= [node] # 현재 집합에 대한 스택

    while stack:
        current_node= stack.pop()
        visited[current_node]= True
        for idx, connected in enumerate(computers[current_node]):
            if connected and visited[idx]==False:
                stack.append(idx)

def solution(n, computers):
    answer= 0
    visited= [False]*n
    for i in range(n):
        if not visited[i]: # 노드가 방문되지 않았으면, 즉 집합을 이루지 못했으면 dfs로 집합을 찾고 +1(answer)
            dfs(computers, visited, i)
            answer+= 1

    return answer

print(solution(3, [[1,1,0], [1,1,0], [0,0,1]]))
print(solution(3, [[1,1,0], [1,1,1], [0,1,1]]))