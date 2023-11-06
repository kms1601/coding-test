from itertools import combinations

def solution(numbers):
    result = set()
    pair = combinations(numbers, 2)
    
    for i, j in pair:
        result.add(i + j)

    return sorted(list(result))
        
print(solution([2,1,3,4,1]))