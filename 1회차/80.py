def solution(amount):
    unit= [100, 50, 10, 1]
    answer= []

    for coin in unit:
        while amount>= coin:
            answer.append(coin)
            amount -= coin

    return answer

print(solution(123))
print(solution(350))