# 내가 짠거
# 정확성은 맞아도 효율성에서 차이난다 ㅠ ㅠ
# 테스트 케이스 마지막에서 시간 초과가 뜬다.
def solution(n):
    # results= set()
    results= []
    directions= [[-1,-1], [-1,1], [1,-1], [1,1]]

    # 대각선 계산
    def cal_diag(idx, num):
        # 0,1
        row, col= idx, num
        diag= []

        for dir in directions:
            is_check= True
            while is_check:
                nidx, nnum= row+dir[0], col+dir[1]

                if 0<=nidx<n and 0<=nnum<n:
                    diag.append((nidx, nnum))
                    row, col = nidx, nnum
                else:
                    is_check= False
                    row, col= idx, num

        return diag

    # 현재 idx가 여태까지의 selected_nums의 대각선 상에 있으면 True
    def is_diag(idx, selected_nums):
        diag=[]
        for nidx, num in enumerate(selected_nums):
            diag.append((nidx,num))
            diag+= cal_diag(nidx, num)
        if (len(selected_nums), idx) in diag: # 대각선:
            return True
        else:
            return False

    def backtrack(selected_nums):
        if len(selected_nums)==n:
            # results.add(tuple(selected_nums))
            # results.append(tuple(selected_nums))
            results.append(selected_nums[:])
            return True # 1

        for i in range(n):
            if i not in selected_nums and is_diag(i, selected_nums)==False:
                selected_nums.append(i)
                if backtrack(selected_nums): # 퀸 배치가 하나 만들어지면
                    selected_nums.remove(i)
                    continue
                selected_nums.remove(i)
        return 0

    backtrack([])

    return len(results)

print(solution(4))