from collections import deque
import heapq
import sys


class node:
    def __init__(self, link, visit):
        self.link = link
        self.visit = visit

    def add_link(self, target):
        heapq.heappush(self.link, target)

    def get_min_link(self):
        if self.link:
            return heapq.heappop(self.link)
        else:
            return False


stack = []
queue = deque()
input = sys.stdin.readline
n, m, v = map(int, input().split())
nodes1 = [node([], False) for i in range(n)]
nodes2 = [node([], False) for i in range(n)]

for _ in range(m):
    num, target = map(int, input().split())
    nodes1[num - 1].add_link(target)
    nodes1[target - 1].add_link(num)
    nodes2[num - 1].add_link(target)
    nodes2[target - 1].add_link(num)

nodes1[v - 1].visit = True
nodes2[v - 1].visit = True

stack.append(nodes1[v - 1])
dfs = [v]
while stack:
    min_link = stack[-1].get_min_link()
    if min_link:
        if not nodes1[min_link - 1].visit:
            stack.append(nodes1[min_link - 1])
            stack[-1].visit = True
            dfs.append(min_link)
    else:
        stack.pop()

queue.append(nodes2[v - 1])
bfs = [v]
while queue:
    min_link = queue[0].get_min_link()
    if min_link:
        if not nodes2[min_link - 1].visit:
            queue.append(nodes2[min_link - 1])
            queue[-1].visit = True
            bfs.append(min_link)
    else:
        queue.popleft()
print(*dfs)
print(*bfs)
