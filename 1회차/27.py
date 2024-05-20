class Node:
    def __init__(self, key):
        self.left= None
        self.right= None
        self.val= key

class BST:
    def __init__(self):
        self.root= None

    def insert(self, key):
        if not self.root:
            self.root= Node(key)
        else: # 루트 노드가 아니면
            curr= self.root
            while True:
                if key < curr.val:
                    if curr.left:
                        curr= curr.left
                    else:
                        curr.left= Node(key)
                        break
                else:
                    if curr.right:
                        curr= curr.right
                    else:
                        curr.right= Node(key)
                        break

    def search(self, key):
        curr= self.root
        while curr and curr.val!= key:
            if key < curr.val:
                curr= curr.left
            else:
                curr= curr.right
        return curr


def solution(lst, search_lst):
    answer= []
    bst= BST()

    for key in lst:
        bst.insert(key)

    for search_val in search_lst:
        if bst.search(search_val):
            answer.append(True)
        else:
            answer.append(False)

    return answer

print(solution([5,3,8,4,2,1,7,10], [1,2,5,6]))