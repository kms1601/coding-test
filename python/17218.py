import sys

input = sys.stdin.readline
N, M = map(int, input().split())
sites = {}

for _ in range(N):
  address, password = input().split()
  sites[address] = password

for _ in range(M):
  print(sites[input().strip()])
  