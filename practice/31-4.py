# 프로그래머스 다른 사람 코드
from collections import deque

def solution(info, edges):
    answer = 0
    n = len(info)
    tree = {i: [] for i in range(n)}
    for p, s in edges:
        tree[p].append(s)
    q = deque([[0, tree[0], 1, 0]])

    while q:
        now, can_move, sheep, wolf = q.popleft()
        if answer < sheep:
            answer = sheep
        for i, node in enumerate(can_move):
            if info[node] == 1: # 늑대면
                if sheep > wolf + 1:
                    q.append([node, can_move[:i] + can_move[i + 1:] + tree[node], sheep, wolf + 1])
            else: # 양이면
                q.append([node, can_move[:i] + can_move[i + 1:] + tree[node], sheep + 1, wolf])
            # can_move[:i] + can_move[i + 1:] + tree[node]: 부모 노드 중에서 현재 노드를 제외하고,현재 노드의 자식을 추가

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))