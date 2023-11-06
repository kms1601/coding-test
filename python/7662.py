import heapq, sys

input = sys.stdin.readline

for _ in range(int(input())):
    dpq = {}
    min_heap = []
    max_heap = []
    idx = 0
    for _ in range(int(input())):
        cmd, arg = input().split()
        arg = int(arg)
        if cmd == "I":
            dpq[idx] = arg
            heapq.heappush(min_heap, (arg, idx))
            heapq.heappush(max_heap, (-arg, idx))
            idx += 1
        elif cmd == "D":
            if min_heap:
                if arg == -1:
                    while True:
                        _, idx = heapq.heappop(min_heap)
                elif arg == 1:
                    var = heapq.heappop(max_heap)
                    min_heap.remove(-var)
    if min_heap:
        print(heapq.heappop(min_heap), -heapq.heappop(max_heap))
    else:
        print("EMPTY")
