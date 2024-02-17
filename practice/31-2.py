# 교재
from collections import deque

def solution(info, edges):
    # 1
    def build_tree(info, edges):
        tree= [[] for _ in range(len(info))]
        for edge in edges:
            tree[edge[0]].append(edge[1])
        return tree

    # 2
    tree= build_tree(info, edges)

    # 3
    maxSheep= 0

    # 4
    q= deque([(0,1,0,set())])

    while q:
        # 5
        cur, sheep, wolf, visited= q.popleft()
        # 6
        maxSheep= max(maxSheep, sheep)
        # 7
        visited.update(tree[cur]) # visited: 부모의 자식 노드들

        # 8
        for next_node in visited:
            if info[next_node] == 1: # 늑대면
                if sheep != wolf+1: # 자식 노드로 내려가도 ㄱㅊ으면
                    q.append(
                        (next_node, sheep, wolf+1, visited-{next_node})
                        )
            else: # 양이면
                q.append(
                    (next_node, sheep+1, wolf, visited-{next_node})
                )

    return maxSheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))