# 교재

def find(parent, i):
    if parent[i] == i:
        return i # 찾는 노드가 루트 노드
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot= find(parent, x)
    yroot= find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot]= yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot]= xroot
    else:
        # 두 랭크가 같은 경우
        parent[yroot]= xroot
        rank[xroot]+=1

def solution(n, costs):
    costs.sort(key= lambda x: x[2])
    parent= list(range(n)) # 섬(노드)의 번호
    minCost= 0 # 최소 비용
    edges= 0 # 다리 개수
    rank= [0]*n # 트리 노드의 랭크

    # 사이클은 다 무시하고 다리가 n-1 개가 될 때까지 집합 형성

    for edge in costs:
        if edges == n-1:
            break

        xroot= find(parent, edge[0])
        yroot= find(parent, edge[1])

        if xroot!= yroot: # 사이클 방지
            union(parent, rank, xroot, yroot)
            minCost+= edge[2]
            edges+= 1

    return minCost

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))