# 프로그래머스 다른 사람 코드

preorder = list() # 귀찮아서 전역으로 # 전위
postorder = list() # 후위
def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6) # 재귀 호출 깊이 제한
    levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
    nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
    # print('nodes: ', nodes)
    # nodes:  [(7, [8, 6]), (4, [3, 5]), (2, [11, 5]), (6, [1, 3]), (1, [5, 3]), ...]
    order(nodes,levels,0)
    return [preorder,postorder]

def order(nodes,levels,curlevel): # 재귀 호출
    n = nodes[:] # copy
    cur = n.pop(0) # VISIT # cur[0]: 노드 번호, cur[1][0]: x좌표, cur[1][1]: y좌표
    preorder.append(cur[0]) # PRE-ORDER: top -> left -> right
    if n: # stop if leaf node
        for i in range(len(n)): # find next floor, 노드 하나씩
            if n[i][1][1] == levels[curlevel+1]: # next floor, 좌변: y좌표
                if n[i][1][0] < cur[1][0]: # LEFT CHILD이면
                    order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
                else: # RIGHT CHILD
                    order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
                    break
    postorder.append(cur[0]) # POST-ORDER

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])) # 노드 9개