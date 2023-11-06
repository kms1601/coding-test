import heapq
import sys

input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    inp = int(input().strip())
    if inp:
        heapq.heappush(heap, inp)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
