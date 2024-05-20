# 직접
from collections import defaultdict
def solution(n, wires):
    answer= float('inf')

    # 인접 리스트
    adj_list=defaultdict(list)
    for u, v in wires:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def dfs(node, visited): # 1. DFS(재귀 함수 이용)
        visited.add(node)
        for adj in adj_list.get(node, []):
            if adj not in visited:
                dfs(adj, visited)
        return len(visited)

    for wire in wires: # 2. 두 집합의 개수의 차(diff)가 기존 차이 값(answer)보다 작으면 갱신
        visited = set()
        adj_list[wire[0]].remove(wire[1])
        adj_list[wire[1]].remove(wire[0])

        a= dfs(wire[0], visited)
        b= n-a
        diff= (a-b if a>b else b-a)
        answer= (diff if diff<answer else answer)

        adj_list[wire[0]].append(wire[1])
        adj_list[wire[1]].append(wire[0])

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))