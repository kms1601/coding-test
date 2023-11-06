import sys

input = list(map(int, sys.stdin.readline().split()))
print('<' if input[0] < input[1] else '>' if input[0] > input[1] else '==')