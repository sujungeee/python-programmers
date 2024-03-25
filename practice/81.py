# 교재 + 내가 수정
# 이게 for에 while이 아닌 if가 들어가면 items이 한번 돌면 가치 환산이 끝남.
# 그러면 weight가 모든 items의 무게의 합보다 크면 남은 무게에 대한 가치가 책정이 안됨
# 그래서 while을 넣어서 remaining_weight가 무게 당 가치가 큰 item으로 가능할 때까지 소모되어야 함
# 모두 소모시키면 다음 가치가 가장 높은 item의 fraction 만큼 남은 가치를 더하고 break

def calculate_unit_value(items):
    for item in items:
        item.append(item[1]/item[0])
    return items

def sort_by_unit_value(items):
    items.sort(key= lambda x:x[2], reverse=True)
    return items

def main(items, weight_limit):
    total_value= 0 # 가치: item[1]
    remaining_weight= weight_limit

    for item in items:
        while item[0] <= remaining_weight:
            total_value += item[1]
            remaining_weight -= item[0]
        if item[0] > remaining_weight:
            fraction= remaining_weight/item[0]
            total_value+= item[1]*fraction
            break
    return total_value

def solution(items, weight_limit):
    items= calculate_unit_value(items)
    items= sort_by_unit_value(items)

    return main(items, weight_limit)

print(solution([[10,19], [7,10], [6,10]], 115))
print(solution([[10,60], [20,100], [30,120]], 50))