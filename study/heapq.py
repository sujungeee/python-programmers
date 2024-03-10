# heapq 공부
# + 이중 우선 순위 큐 공부(0311)
# ref #1 https://littlefoxdiary.tistory.com/3
# ref #2 https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99
# ref #3 https://seongonion.tistory.com/91
import heapq

# 1. heapify
list1= [10,3,5,8,1]
heapq.heapify(list1)
# print(list1) # [1, 3, 5, 8, 10]

# 2. heappush, heappop with 최소힙, 최대힙
# 2-1. default: 최소 힙
heap= [[1,2,3], [7,8,9], [4,5,6]]
heapq.heappush(heap, [1,5,3])
heapq.heappush(heap, [2,4,6])
# print('heap(push 후): ', heap) # [[1, 2, 3], [1, 5, 3], [4, 5, 6], [7, 8, 9], [2, 4, 6]]
heapq.heappop(heap)
# print('heap(pop 후): ', heap) # [[1, 5, 3], [2, 4, 6], [4, 5, 6], [7, 8, 9]]
# heappop: 가장 작은 원소를 힙에서 제거한 후 다시 힙 정렬을 진행

# 2-2. 최대 힙 만들기
tmp_heap= [] # - 들을 넣어놓는 임시 힙
max_heap= [] # 최대 힙
for item in heap:
    heapq.heappush(tmp_heap, [i*-1 for i in item])
# print(tmp_heap) # [[-7, -8, -9], [-4, -5, -6], [-2, -4, -6], [-1, -5, -3]]

for _ in range(len(heap)):
    tmp= heapq.heappop(tmp_heap)
    max_heap.append([i*-1 for i in tmp])
# print(max_heap) # [[7, 8, 9], [4, 5, 6], [2, 4, 6], [1, 5, 3]]

# 3. nlargest, nsmallest: 힙의 n개의 가장 큰 리스트, n개의 가장 작은 리스트
print(heap) # [[1, 5, 3], [2, 4, 6], [4, 5, 6], [7, 8, 9]]
print(heapq.nlargest(n=2, iterable=heap)) # [[7, 8, 9], [4, 5, 6]]
print(heapq.nsmallest(n=3, iterable=heap)) # [[1, 5, 3], [2, 4, 6], [4, 5, 6]]