def solution(X, Y):
    num_list_X = [0 for _ in range(10)]
    num_list_Y = [0 for _ in range(10)]
    couple = [0 for _ in range(10)]
    answer = []
    for s in X:
        num_list_X[int(s)] += 1
    for s in Y:
        num_list_Y[int(s)] += 1
    for idx, (x, y) in enumerate(zip(num_list_X, num_list_Y)):
        if x and y:
            couple[idx] = min([x, y])
    for idx, cnt in enumerate(couple[::-1]):
        answer.extend([str(9 - idx) for _ in range(cnt)])
        
    if answer:
        return int("".join(answer))
    else:
        return -1


print(solution("12321", "42531"))
