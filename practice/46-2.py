# 교재
def solution(n, wires):
    graph= [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, parent):
        cnt= 1
        for child in graph[node]:
            if child!= parent:
                cnt+= dfs(child, node)
        return cnt

    min_diff= float('inf')
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        cnt_a= dfs(a,b)
        cnt_b= n-cnt_a

        min_diff= min(min_diff, abs(cnt_a-cnt_b))

        graph[a].append(b)
        graph[b].append(a)

    return min_diff

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))