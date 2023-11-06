from collections import deque

def solution(board):
    queue = deque()
    size = len(board)
    visit = [[-1] * size for _ in board]
    dydx = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue.append([0, 0, (1, 0), 0])
    
    while queue:
        x, y, past, cost = queue.popleft()
        for dy, dx in dydx:
            ny = y + dy
            nx = x + dx
            
            if ny < 0 or ny > size - 1 or nx < 0 or nx > size - 1 or board[ny][nx] == 1: continue
            
            if past == (dy, dx):
                ncost = cost + 100
            else:
                ncost = cost + 600
                
            if visit[ny][nx] == -1 or ncost < visit[y][x]:
                visit[0][0] == ncost
                queue.append([ny, nx, (dy, dx), ncost])
        print(visit[0][0])
solution([[0,0,0],[0,0,0],[0,0,0]])