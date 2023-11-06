import sys

times = int(sys.stdin.readline())
queue = []
for _ in range(times):
    queue.append(list(map(int, sys.stdin.readline().split())))
for i in queue:
    print(i[0] + i[1])