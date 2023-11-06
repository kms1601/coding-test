def hanoi(plates, start, mid, end, answer):
    if plates == 1:
        return answer.append([start,end])
    hanoi(plates - 1, start, end, mid, answer)
    answer.append([start, end])
    hanoi(plates - 1, mid, start, end, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

print(solution(2))