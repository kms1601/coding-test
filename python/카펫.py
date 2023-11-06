def solution(brown, yellow):
    area = brown + yellow
    for length in [i for i in range(3, int(area**(1 / 2)) + 1) if area % i == 0]:
        if 2 * length + 2 * area / length - 4 == brown:
            return [int(area / length), length]
        
        
print(solution(10, 2))