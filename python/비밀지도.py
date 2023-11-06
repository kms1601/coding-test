def solution(n, arr1, arr2):
    combined = []
    answer = []
    for i, j in zip(arr1, arr2):
        combined.append(i | j + 2**n)
    for line in combined:
        tmp = []
        for tresure in bin(line)[3:]:
            if tresure == "1":
                tmp.append("#")
            else:
                tmp.append(" ")
        answer.append("".join(tmp))
    return answer


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
