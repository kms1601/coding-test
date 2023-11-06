import sys


input = sys.stdin.readline
k, n = map(int, input().split())
answer = 0

lan_list = []
for _ in range(k):
    lan_list.append(int(input()))

left, right = 1, max(lan_list)

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for lan in lan_list:
        cnt += lan // mid
    
    if cnt < n:
        right = mid - 1
    elif cnt >= n:
        answer = mid
        left = mid + 1
print(answer)
