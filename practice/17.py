from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1= deque(cards1)
    cards2= deque(cards2)
    goal= deque(goal)
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            answer='No'
            break
    return answer

print(solution(["i","drink","water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))