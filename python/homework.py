import sys

homework = [0] * 30
for i in range(28):
    num = int(sys.stdin.readline())
    homework[num - 1] = 1
for i in range(30):
    if homework[i] == 0:
        print(i + 1)