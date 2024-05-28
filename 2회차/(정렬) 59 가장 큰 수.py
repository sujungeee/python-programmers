from functools import cmp_to_key

def compare(x, y):
    if x+y > y+x:
        return -1 # x가 y 앞에 위치
    elif x+y == y+x:
        return 0 # x와 y가 동일
    else:
        return 1 # y가 x 앞에 위치
def solution(numbers):
    result= ''

    for i in range(len(numbers)):
        numbers[i]= str(numbers[i])
    numbers.sort(key= cmp_to_key(compare))

    for num in numbers:
        result+=num
    if int(result)==0:
        result= '0'
    return result

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))