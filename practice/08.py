def solution(s):
    ans=[]
    for i in s:
        if i=='(':
            ans.append(i)
        elif i==')':
            if not ans: # 열린 괄호 없이 닫힌 괄호만 있으면 False를 반환
                return False
            else:
                ans.pop()
    if ans: # ans 리스트에 요소가 존재하면 상쇄되지 못한 괄호가 존재한다는 의미이므로 False를 반환
        return False
    else:
        return True

print(solution('(())()'))