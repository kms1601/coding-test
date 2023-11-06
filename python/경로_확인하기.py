def solution(move):
    pos = [0, 0]
    visit = {}
    
    for dir in move:
        if dir == 'U': 
            if pos[1] < 5:
                pos[1] += 1
                visit[f'y{pos[1] - 1, pos[1], pos[0]}'] = 1
            else: pass
        if dir == 'D':
            if pos[1] > -5:
                pos[1] -= 1
                visit[f'y{pos[1], pos[1] + 1, pos[0]}'] = 1
            else: pass
        if dir == 'R':
            if pos[0] < 5:
                pos[0] += 1
                visit[f'x{pos[0] - 1, pos[0], pos[1]}'] = 1
            else: pass
        if dir == 'L':
            if pos[0] > -5:
                pos[0] -= 1
                visit[f'x{pos[0], pos[0] + 1, pos[1]}'] = 1
            else: pass
    return len(visit)
    

print(solution(['U', 'R', 'U', 'L', 'D', 'L', 'D', 'U']))