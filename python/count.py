import sys

a = int(sys.stdin.readline())
if a != 1:
    b = list(map(int, sys.stdin.readline().split()))
    c = int(sys.stdin.readline())
    print(b.count(c))
else:
    if sys.stdin.readline() == sys.stdin.readline():
        print(1)
    else:
        print(0)