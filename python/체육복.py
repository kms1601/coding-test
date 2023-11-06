def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve.sort()
    for lent in reserve[:]:
        if lent in lost:
            answer += 1
            lost.remove(lent)
            reserve.remove(lent)
    for lent in reserve:
        if lent - 1 in lost:
            answer += 1
            lost.remove(lent - 1)
        elif lent + 1 in lost:
            answer += 1
            lost.remove(lent + 1)
    return answer


print(solution(5, [4, 5], [3, 4]))
