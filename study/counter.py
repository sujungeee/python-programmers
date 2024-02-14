from itertools import combinations
from collections import Counter

orders= ["BACGF", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course= 2

menu= []

for order in orders:
    menu+= combinations(sorted(order), course)

counter= Counter(menu)
print('그냥 counter: ', counter)
counter = Counter(menu).most_common()
print('most counter: ', counter)
