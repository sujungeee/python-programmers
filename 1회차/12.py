def solution(prices):
    n= len(prices)
    stack = []
    answer=[0]*n
    for index in range(n):
        # 스택에서 pop하는 조건
        # 이전 값이 현재 값보다 클 때, 스택에 무언가 있을 때(이전 값이 현재 값과 같거나 작으면 pop 멈추기)
        while(stack and prices[stack[-1]]>prices[index]):
            a= stack.pop()
            answer[a]=index-a
        # 스택에서 push하는 조건
        stack.append(index)
    # for 다 마쳤는데 남아있는 인덱스에 대한 처리
    while stack:
        a= stack.pop()
        answer[a]= n-a-1
    return answer

print(solution([1,2,3,2,3]))