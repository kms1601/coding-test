import sys

a, b = map(int, sys.stdin.readline().split())
input2 = map(int, sys.stdin.readline().split())

for i in input2:
    if i < b:
        print(i, end = ' ')