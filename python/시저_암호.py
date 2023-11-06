def solution(s, n):
    result = ''
    for char in s:
        if char == ' ':
            result += ' '
        elif ord(char) >= 65 and ord(char) <= 90:
             result += chr(ord(char) + n if ord(char) + n <= 90 else ord(char) + n - 26)
        elif ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) + n if ord(char) + n <= 122 else ord(char) + n - 26)
    return result
print(solution("a B z", 4))

#A-Z - 65 - 90
#a-z - 97 - 122