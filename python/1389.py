import sys
from collections import deque


input = sys.stdin.readline
n, m = map(int, input().split())
link = {i: [] for i in range(1, n + 1)}
kevin_list = []


for _ in range(m):
    start, end = map(int, input().split())
    link[start].append(end)
    link[end].append(start)

for me in range(1, n + 1):
    kevin = 0
    for target in range(1, n + 1):
        queue = deque()
        queue.append([me, 0])

        while True:
            start = queue.popleft()
            if start[0] == target:
                break
            for end in link[start[0]]:
                queue.append([end, start[1] + 1])
        kevin += start[1]
    kevin_list.append(kevin)
print(kevin_list.index(min(kevin_list)) + 1)
