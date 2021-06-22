# priority queue implementation using heapq
import heapq

heap = [4, 7, 3, -2, 1, 0]

heapq.heapify(heap)

print(heap)
print('_______________')
nums = [3, 2, -9, 44, -14, 0, 14]
heap=[]

for value in nums:
    heapq.heappush(heap,value)

while heap:
    print(heapq.heappop(heap))
