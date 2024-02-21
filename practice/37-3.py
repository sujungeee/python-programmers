# 크루스칼 알고리즘: 그리디 알고리즘의 일종
# https://chanhuiseok.github.io/posts/algo-33/
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def solution(n, costs):
    answer= 0 # 최소 비용
    edges= sorted([ (x[2], x[0], x[1]) for x in costs]) # cost, x, y
    parent= list(range(n))

    bridges= 0 # 다리 개수

    for cost,x,y in edges:
        # 두 집합이 다르면 union!! 여기서 집합 더하기(따로 함수 안빼고)
        if find(parent, x) != find(parent, y):
            answer+= cost
            bridges+= 1
            parent[find(parent,x)]= y # x의 루트 노드의 부모를 y로 하여 union
        if bridges == n-1:
            break
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))