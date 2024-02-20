# 전위, 중위, 후위의 개념
# https://velog.io/@koreanthuglife/%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-%EC%A0%84%EC%9C%84-%ED%9B%84%EC%9C%84-%EC%A4%91%EC%9C%84
class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info= info
        self.num= num
        self.left= left
        self.right= right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

def bt(nodeinfo): # (좌표 - 노드 번호) 연결시켜야 함. => [Class] Node
    # 노드 번호 배열
    nodeNum= [i+1 for i in range(len(nodeinfo))]
    nodeNum.sort(key=lambda x:(-nodeinfo[x-1][1], nodeinfo[x-1][0])) # 1 idx는 내림차순, 2 idx는 오름차순

    # 노드 번호끼리 연결시킬 이진 트리: bntree
    bntree= None
    for i in range(len(nodeNum)):
        if bntree == None: # 처음 루트 노드 추가
            bntree= Node(nodeinfo[nodeNum[0]-1], nodeNum[0]) # 노드 좌표, 노드 번호
        else:
            parent= bntree
            node= Node(nodeinfo[nodeNum[i]-1], nodeNum[i])

            while True: # 본인의 삽입 위치를 찾을 때까지
                if node.info[0] < parent.info[0]:
                    if parent.has_left():
                        parent= parent.left
                        continue
                    else: # 자신이 왼쪽 노드가 되어 삽입
                        parent.left= node
                        break
                if node.info[0] > parent.info[0]:
                    if parent.has_right():
                        parent= parent.right
                        continue
                    else:
                        parent.right= node
                        break

    return bntree

def pre_order(bntree):
    order = []
    stack = [bntree]
    while stack:
        node = stack.pop()
        if node is None:  # 자식 노드가 존재하지 않으면
            continue
        order.append(node.num) # top은 먼저 append
        stack.append(node.right) # right
        stack.append(node.left) # left
    return order

def post_order(bntree):
    order= []
    stack= [(bntree, False)]

    while stack:
        node, visited= stack.pop()

        if node is None:
            continue
        if visited:
            order.append(node.num)
        else:
            stack.append((node, True)) # top
            stack.append((node.right, False)) # right
            stack.append((node.left, False)) # left

    return order

def solution(nodeinfo):
    answer=[]
    bntree= bt(nodeinfo) # 노드 번호와 좌표로 이진트리 생성
    # 전위 순회
    answer.append(pre_order(bntree))

    # 후위 순회
    answer.append(post_order(bntree))

    return answer

# print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])) # 노드 9개