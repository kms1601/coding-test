def solution(n):
    for num in range(2, n + 1):
        if ((n - 1) / num).is_integer():
            print(num)
            break
