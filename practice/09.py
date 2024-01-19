def solution(decimal):
    stack=[] # 나머지를 넣을 stack
    while decimal>0:
        remainder= decimal%2
        stack.append(str(remainder))
        decimal //= 2
    binary=''.join(stack[::-1]) # stack[-1:len(stack)-1:-1], 즉 stack[-1:-5:-1] == stack[::-1]
    # step이 음수일려면 stop 인덱스가 start 인덱스보다 작아야 한다.
    return binary

print(solution(10))