def solution(sequence, k):
    left, right = 0, 0
    min_len = float("inf")
    answer = [0, 0]
    while right < len(sequence):
        sum_ = sum(sequence[left:right + 1])
        if sum_ < k:
            right += 1
        elif sum_ > k:
            left += 1
        else:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                answer[0], answer[1] = left, right
            left += 1
    return answer
print(solution([1, 1, 1, 2, 3, 4, 5], 5))