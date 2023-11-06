import sys

N, M = map(int, sys.stdin.readline().split())
basket = [i + 1 for i in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    basket[a - 1], basket[b - 1] = basket[b - 1], basket[a - 1]
for i in basket:
    print(i, end = ' ')