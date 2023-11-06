import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N
for i in range(M):
    start, end, num = map(int, sys.stdin.readline().split())
    for j in range(start - 1, end):
        basket[j] = num
for i in basket:
    print(i, end = ' ')