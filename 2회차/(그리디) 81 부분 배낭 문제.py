from collections import deque
def solution(items, weight_limit):
    totalValue= 0
    itemValues= []
    for item in items:
        itemValues.append([item[1]/item[0], item])
    itemValues.sort(reverse= True)

    itemValues= deque(itemValues)

    while weight_limit>0:
        useKg= itemValues.popleft()
        if weight_limit >= useKg[1][0]:
            weight_limit-= useKg[1][0]
            totalValue= totalValue + useKg[1][0]*useKg[0]
        else:
            totalValue= totalValue + weight_limit*useKg[0]
            weight_limit= 0

    if totalValue==int(totalValue):
        return round(totalValue)
    else:
        return round(totalValue,2)

print(solution([[10, 19], [7, 10], [6, 10]], 15))
print(solution([[10, 60], [20, 100], [30, 120]], 50))