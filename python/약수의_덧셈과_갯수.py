def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        cnt = 1
        for n in range(1, num // 2 + 1):
            if num % n == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer


print(solution(13, 17))
