class Node:
    def __init__(self, data=None):
        self.data= data
        self.next= None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insert(self, prev_node, data):
        node= Node(data)
        self.size+=1

        if prev_node:
            node.next=prev_node.next
            prev_node.next= node
        else:
            node.next= self.head
            self.head= node
    def traverse(self):
        current= self.head
        while current:
            yield current.data
            current = current.next

    def delete(self, prev_node):
        self.size -=1
        if prev_node:
            prev_node.next= prev_node.next.next
        else:
            self.head= self.head.next


words= SinglyLinkedList()
words.insert(None, "eggs")
words.insert(words.head, "ham")
words.delete(words.head)
for word in words.traverse():
    print(word)