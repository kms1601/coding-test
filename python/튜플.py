def solution(s):
    result = []
    s = s[2:-2].split('},{')
    s.sort(key=len)
    for element in s:
        element = element.split(',')
        for num in element:
            if not int(num) in result:
                result.append(int(num))
    return result

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))