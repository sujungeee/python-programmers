# 참고 코드(내가 생각했던 로직과 비슷한 코드)
# https://kjhoon0330.tistory.com/entry/프로그래머스-양과-늑대-Python
def getCanGoEdges(i, prev, graph):
    canGoEdges= [edge for edge in prev if edge!= i] # 기존 탐색 인덱스 - 현재 탐색 인덱스(i)
    for j in range(len(graph)):
        if graph[i][j]== True: # 부모 노드 i의 자식 관계이면
            canGoEdges.append(j) # 자식 노드를 추가

    return canGoEdges

def BFS(i, sheep, wolf, prev, graph, info):
    global answer
    cangoEdges= getCanGoEdges(i, prev, graph)
    if sheep == wolf or not cangoEdges:
        if answer < sheep: # 갱신한 sheep 이 더 크면 answer에 sheep(answer는 최대 양의 수 이므로)
            answer= sheep
        return # return이 되면 가장 바깥 DFS를 부른 조건문 밖 for문, 즉 바로 밑 for문으로 돌아감

    for edge in cangoEdges: # 자식 노드에 대해서
        if info[edge] == 0: # 자식 노드가 양인 경우
            BFS(edge, sheep+1, wolf, cangoEdges, graph, info)
        else: # 자식 노드가 늑대인 경우
            BFS(edge, sheep, wolf+1, cangoEdges, graph, info)

def solution(info, edges):
    global answer
    answer= 1 # 루트 노드는 무조건 양이므로
    graph= [[False]*len(info) for _ in range(len(info))] # len(info): 12
    for x, y in edges:
        graph[x][y]= True # x: 부모, y: 자식

    BFS(0, 1, 0, [0], graph, info) # i: 현재 노드의 인덱스

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))