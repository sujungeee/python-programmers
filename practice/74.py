# 교재
# 피보나치 수열

def solution(n):

    fib= [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-1]+fib[i-2])%1234567)

    return fib[n]

print(solution(3))
print(solution(5))