# https://it-garden.tistory.com/326
class DoubleLinkedList:
    class Node:
        def __init__(self, item, prev, link):
            self.item= item
            self.prev= prev
            self.next= link

    def __init__(self):
        self.head= self.Node(None, None, None)
        self.tail= self.Node(None, self.head, None)
        self.head.next= self.tail
        self.size= 0

    def size(self):
        return self.size

    def isempty(self):
        return self.size==0

    def insert_before(self, p, item):
        prevNode= p.prev
        n= self.Node(item, prevNode, p)
        p.prev= n
        prevNode.next= n
        self.size+= 1
    def insert_after(self, p, item):
        nextNode= p.next
        n= self.Node(item, p, nextNode)
        p.next= n
        nextNode.prev= n
        self.size+= 1

    def delete(self, x):
        n1= x.prev
        n2= x.next
        n1.next=n2
        n2.prev= n1
        self.size-= 1
        return x.item

    def print_list(self):
        if self.isempty():
            print('List is empty.')
        else:
            p= self.head.next
            while p!= self.tail:
                if p.next!= self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p= p.next

class EmptyError(Exception):
    pass

s= DoubleLinkedList()
s.insert_after(s.head, 'apple')
s.insert_before(s.tail, 'orange')
s.insert_before(s.tail, 'cherry')
s.insert_after(s.head.next, 'pear')
s.print_list()

print('마지막 노드 삭제 후: \t', end='')
s.delete(s.tail.prev)
s.print_list()

print('맨 끝에 포도 삽입 후: \t', end='')
s.insert_before(s.tail, 'grape')
s.print_list()

print('첫 노드 삭제 후: \t', end='')
s.delete(s.head.next)
s.print_list()

print('두 번째 노드 삭제 후: \t', end= '')
s.delete(s.head.next.next)
s.print_list()

print('첫 노드 삭제 후: \t', end='')
s.delete(s.head.next)
s.print_list()

print('첫 노드 삭제 후: \t', end='')
s.delete(s.head.next)
s.print_list()