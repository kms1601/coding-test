def dicimal_to_ternary_reversed(n):
    result = []
    while n:
        n, remainder = divmod(n, 3)
        result.append(str(remainder))
    return ''.join(result[::-1])

def solution(n):
    answer = 0
    ternary = enumerate(dicimal_to_ternary_reversed(n))
    for digit, num in ternary:
        answer += int(num) * (3 ** int(digit))
    return answer
        
    
print(solution(125))