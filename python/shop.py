import sys

total = int(sys.stdin.readline())
kind = int(sys.stdin.readline())
buy = []
for i in range(kind):
    buy.append(list(map(int, sys.stdin.readline().split())))
buy = list(map(lambda x: x[0] * x[1], buy))
if sum(buy) == total:
    print('Yes')
else:
    print('No')