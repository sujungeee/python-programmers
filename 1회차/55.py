# 교재(병합 정렬)

def solution(arr1, arr2):
    sortarr= []
    i, j = 0,0

    while (i<len(arr1) and j<len(arr2)):
        if arr1[i] <= arr2[j]:
            sortarr.append(arr1[i])
            i+=1
        else:
            sortarr.append(arr2[j])
            j+=1

    # 내가 짠 나머지 추가
    # if i == len(arr1):
    #     for ridx in range(j, len(arr2)):
    #         sortarr.append(arr2[ridx])
    # else:
    #     for ridx in range(i, len(arr1)):
    #         sortarr.append(arr1[ridx])

    # 교재가 짠 나머지 추가
    while i<len(arr1):
        sortarr.append(arr1[i])
        i+=1

    while j<len(arr2):
        sortarr.append(arr2[j])
        j+=1

    return sortarr

print(solution([1,3,5], [2,4,6]))
print(solution([1,2,3], [4,5,6]))

