from itertools import combinations
from collections import Counter

orders= ["XYZ", "XWY", "WXA"]
courses= [2,3,4]

for course in courses:
    menu= []

    for order in orders:
        menu+= combinations(sorted(order), course)

    counter = Counter(menu).most_common()
    print(counter)
