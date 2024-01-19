stack=[]
max_size=10

def isFull(stack): # true 이면 스택이 가득 차 있는 상태
    return len(stack)==max_size

def isEmpty(stack): # true 이면 스택이 비어있는 상태
    return len(stack)==0

def push(stack, item): # stack에 item을 push
    if isFull(stack):
        print('스택이 가득 찼습니다.')
    else:
        stack.append(item)
        print('데이터가 추가되었습니다.')

def pop(stack, item):
    if isEmpty(stack):
        print('스택이 비어있습니다')