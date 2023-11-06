def solution(s):
    count_zero = 0
    change = 0
    while not s == '1':
        count_zero += s.count('0')
        s = s.replace('0', '')
        temp = bin(len(s))
        s = str(temp[2:])
        change += 1
    return [change, count_zero]

    
print(solution('1111111'))