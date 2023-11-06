import sys

input1 = sys.stdin.readline()
input2 = list(map(int, sys.stdin.readline().split()))
print(min(input2), max(input2))