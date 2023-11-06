def solution(s: str):
    tmp = []
    answer = []
    for char in s:
        if 65 <= ord(char) <= 90:
            tmp.append((char, 0))
        else:
            tmp.append((char, 1))
    tmp.sort(key=lambda x: (x[1], x[0]), reverse=True)
    for char in tmp:
        answer.append(char[0])
    return "".join(answer)
    
print(solution("Zbcdefg"))