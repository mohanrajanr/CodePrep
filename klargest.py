import heapq

array = [3, 4, 5, 6, 2, 1]
array = list(map(lambda x: -x, array))
k = 5

heapq.heapify(array)
print(array)
a = 0
while k:
    a = heapq.heappop(array)
    print(a)
    print(array)
    k -= 1

print(a)