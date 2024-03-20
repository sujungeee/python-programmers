def solution(n):
    return int(''.join(sorted(n.__str__(), reverse= True)))

print(solution(118372))