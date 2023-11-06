import sys

n = int(sys.stdin.readline())
input = []
for _ in range(n):
    input.append(list(map(int, sys.stdin.readline().split())))
for i in input:
    print(i[0] + i[1])