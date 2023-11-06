def collatz(num, count):
    if num == 1: return count
    if count == 500: return -1
    if num % 2 == 0: return collatz(num / 2, count + 1)
    elif num % 2 == 1: return collatz(num * 3 + 1, count + 1)

def solution(num):
    answer = collatz(num, 0)
    return answer

print(solution(6))