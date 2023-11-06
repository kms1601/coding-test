from collections import deque


def solution(maps):
    DRDC = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque()
    ROW, COL = len(maps), len(maps[0])
    visit = [[False] * COL for _ in range(ROW)]
    can_escape = False
    for row, line in enumerate(maps):
        for col, dot in enumerate(line):
            if dot == "S":
                queue.append([row, col, 0])
                visit[row][col] = True
            elif dot == "L":
                lever = [row, col]
            elif dot == "E":
                exit = [row, col]
    while queue:
        row, col, times = queue.popleft()
        if [row, col] == lever:
            lever.append(times)
            can_escape = True
            break
        for dr, dc in DRDC:
            nr = dr + row
            nc = dc + col
            if (
                0 <= nr < ROW
                and 0 <= nc < COL
                and maps[nr][nc] != "X"
                and not visit[nr][nc]
            ):
                visit[nr][nc] = True
                queue.append([nr, nc, times + 1])
    if not can_escape:
        return -1
    queue.clear()
    queue.append(lever)
    visit = [[False] * COL for _ in range(ROW)]
    can_escape = False
    while queue:
        row, col, times = queue.popleft()
        if [row, col] == exit:
            can_escape = True
            break
        for dr, dc in DRDC:
            nr = dr + row
            nc = dc + col
            if (
                0 <= nr < ROW
                and 0 <= nc < COL
                and maps[nr][nc] != "X"
                and not visit[nr][nc]
            ):
                visit[nr][nc] = True
                queue.append([nr, nc, times + 1])
    if not can_escape:
        return -1
    else:
        return times

print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	))