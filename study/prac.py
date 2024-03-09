from collections import deque

dq= deque()
dq.append(1)
dq.append(2)
print(dq) # deque([1, 2])
dq.pop()
print("pop: ", dq)
dq.remove(1)
print(dq) # deque([2])
dq.append(1)
print(dq) # deque([2, 1]) # 2(먼저) -> 1(나중)
print(dq.popleft()) # 2
print(dq) # deque([1])

x= 3
y= 4
maps= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
visited= [[False]*y for i in range(x)]
print(visited)