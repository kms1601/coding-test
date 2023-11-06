from itertools import permutations

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**(1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number_set = set()
    
    for num in range(1, len(numbers) + 1):
        permu = list(permutations([i for i in numbers], num))
        for n in permu:
            number_set.add(int(''.join(n)))

    for num in number_set:
        if is_prime(int(num)):
            answer += 1
    return answer

print(solution("011"))