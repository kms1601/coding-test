def solution(n):
    repeat = 0
    original_n = n
    number = 1
    triangle = [['.'] * i for i in range(1, n + 1)]
    
    while True:
        for i in range(n):
            triangle[i + 2 * repeat][repeat] = number
            number += 1

        n -= 1
        if not n: break
    
        for i in range(n):
            triangle[original_n - repeat - 1][i + repeat + 1] = number
            number += 1

        n -= 1
        if not n: break
        
        for i in range(n):
            triangle[original_n - repeat - 2 - i][original_n - 2 * repeat - 2 - i] = number
            number += 1

        n -= 1
        if not n: break
        
        repeat += 1
    print(triangle)
       
    return sum(triangle, [])