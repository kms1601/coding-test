def solution(rows, columns, queries):
    square = []
    min_value = []
    result = []
    
    for row in range(rows):
        square.append([i + 1 + row * columns for i in range(columns)])
    
    for query in queries:
        for i in range(query[3] - query[1]):
            min_value.append(square[query[0] - 1][query[1] - 1 + i])
            min_value.append(square[query[2] - 1][query[3] - 1 - i])
        
        for i in range(query[2] - query[0]):
            min_value.append(square[query[2] - 1 - i][query[1] - 1])
            min_value.append(square[query[0] - 1 + i][query[3] - 1])
        
        result.append(min(min_value))
        min_value.clear()
        
        ur = square[query[0] - 1][query[3] - 1]
        dr = square[query[2] - 1][query[3] - 1]
        dl = square[query[2] - 1][query[1] - 1]
        ul = square[query[0] - 1][query[1] - 1]
        
        for i in range(1,query[3] - query[1]):
            square[query[0] - 1][query[3] - i] = square[query[0] - 1][query[3] - 1 - i]
            square[query[2] - 1][query[1] - 2 + i] = square[query[2] - 1][query[1] - 1 + i]
        
        for i in range(1,query[2] - query[0]):
            square[query[2] - i][query[3] - 1] = square[query[2] - 1 - i][query[3] - 1]
            square[query[0] - 2 + i][query[1] - 1] = square[query[0] - 1 + i][query[1] - 1]
        
        square[query[0]][query[3] - 1] = ur
        square[query[2] - 1][query[3] - 2] = dr
        square[query[2] - 2][query[1] - 1] = dl
        square[query[0] - 1][query[1]] = ul
        
    return (result)

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))