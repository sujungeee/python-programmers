class LinkedList:
    class Node:
        def __init__(self, num, prev):
            self.num= num
            self.prev= prev
            self.next= None

    def __init__(self, num, start):
        self.root= self.Node(0, None)
        self.current= None # 현재 노드
        self.stack= []
        temp= self.root
        for i in range(1, num):
            new_node= self.Node(i, temp)
            temp.next= new_node
            if i == start:
                self.current= new_node
            temp= new_node

    def up(self, num):
        for _ in range(num):
            if self.current.prev:
                self.current= self.current.prev

    def down(self, num):
        for _ in range(num):
            if self.current.next:
                self.current= self.current.next

    def remove(self):
        remove_node= self.current
        self.stack.append(remove_node)
        if remove_node.next: # 삭제 노드가 맨 아래 행이 아니라면
            self.current= remove_node.next # 현재 행을 아랫 행으로 바꾸고
            self.current.prev= remove_node.prev # 현재 행의 prev를 삭제 행의 prev와 연결
            if remove_node== self.root: # 삭제 노드가 맨 위(0)의 행이라면
                self.root= remove_node.next # 1행이 root가 됨
            if remove_node.prev: # 삭제 노드가 0행이 아니면
                remove_node.prev.next= self.current # 삭제 행의 prev의 next를 현재행과 연결
        else: # 삭제 노드가 맨 아래 행이라면
            self.current= remove_node.prev
            self.current.next= None

    def recover(self):
        recover_node= self.stack.pop()
        if recover_node.prev:
            recover_node.prev.next= recover_node
        if recover_node.next:
            recover_node.next.prev= recover_node
            if recover_node.next== self.root:
                self.root= recover_node

    def get_root(self):
        return self.root

    def __bool__(self):
        return True

def solution(n, k, cmd):
    table= LinkedList(n, k)
    for c in cmd:
        if c[0] == 'U':
            table.up(int(c[2]))
        elif c[0] == 'D':
            table.down(int(c[2]))
        elif c == 'C':
            table.remove()
        else:
            table.recover()

    node= table.get_root()
    answer= ['X']*n
    while node: # 존재하는 행 번호는 O 로 바꾸기
        answer[node.num]= 'O'
        node= node.next
    return "".join(answer)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))