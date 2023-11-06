import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()
for num in b[::-1]:
    print(int(num) * a)
print(a * int(b))