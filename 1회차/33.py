def find(parents, x):
    if parents[x] == x: # 찾는 노드가 루트 노드이면
        return x
    else:
        return find(parents, parents[x])

def union(parents, x, y):
    root1= find(parents, x)
    root2= find(parents, y)
    pNum= max(x, y)
    if pNum == x:
        parents[root2]= root1
    else:
        parents[root1]= root2

def solution(k, operations):
    parents= list(range(k))
    answer= k

    for op in operations:
        if op[0] == 'u':
            union(parents, op[1], op[2])
        elif op[0] == 'f':
            print('find: ', find(parents, op[1]))

    # 집합의 개수 = 루트 노드의 개수(union을 다 하고 총 집합의 수)
    answer= len(set(find(parents, i) for i in range(k)))

    return answer

print(solution(3, [['u',0,1], ['u',1,2], ['f',2]]))
print(solution(4, [['u',0,1], ['u',2,3], ['f',0]]))