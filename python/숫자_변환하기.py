from collections import deque

def solution(x, y, n):
    OPER = (f"+{n}", "*2", "*3")
    visit = [False for _ in range(y)]
    queue = deque([[x, 0]])
    visit[x-1] = True
    while queue:
        num, cnt = queue.popleft()
        if num == y:
            break
        for oper in OPER:
            nnum = eval(str(num) + oper)
            if nnum < y and not visit[nnum-1]:
                visit[nnum-1] = True
                queue.append([nnum, cnt + 1])
            elif nnum == y:
                return cnt + 1
    return -1

print(solution(2, 5,	4))