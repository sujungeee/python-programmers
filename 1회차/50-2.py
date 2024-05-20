# 교재- 백트래킹
# 별도의 board를 만들지 않고 대각선 체크
# 앞으로 효율성이 부족한 아이디어가 첫 번째로 생각났다면
# 효율성이 더 좋게 구현할 수 있는 창의적인 아이디어가 있는지 생각해보기

def getAns(n, y, width, diag1, diag2):
    ans = 0
    if y==n:
        ans= 1
    else:
        for i in range(n): # y: 행, i: 열
            if width[i] or diag1[i+y] or diag2[i-y+n]: # 해당 열에 퀸이 있으면 or 대각선에 퀸이 있으면
                continue

            width[i]= diag1[i+y]= diag2[i-y+n]= True
            ans+= getAns(n, y+1, width, diag1, diag2)
            width[i]= diag1[i+y] = diag2[i-y+n] = False
    return ans

def solution(n):
    ans= getAns(n, 0, [False]*n, [False]*(n*2), [False]*(n*2))
    return ans

print(solution(4))