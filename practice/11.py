def solution(s):
    stack=[]
    for c in s:
        if stack and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack) # 스택이 비어있으면 true이므로 1 반환

print(solution('baabaa'))