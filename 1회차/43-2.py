# 2. 교재
# 그래프로 DFS를 진행(재귀 함수 이용)
def dfs(computers, visited, node):
    visited[node]= True
    for idx, connected in enumerate(computers[node]): # node의 연결 상태
        if connected and visited[idx]==False:
            dfs(computers, visited, idx)
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