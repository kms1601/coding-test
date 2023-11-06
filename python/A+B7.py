import sys

n = int(sys.stdin.readline())
input = []
for _ in range(n):
    input.append(list(map(int, sys.stdin.readline().split())))
for i in range(len(input)):
    print(f'Case #{i + 1}: {input[i][0] + input[i][1]}')