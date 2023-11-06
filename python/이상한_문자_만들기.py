def solution(s):
    result = []
    word_start = -1
    for index, char in enumerate(s):
        if char == ' ':
            word_start = -1
            result.append(char)
        else:
            if not word_start + 1: word_start = index
            if (index - word_start) % 2 == 0: result.append(char.upper())
            else: result.append(char.lower())
    return ''.join(result)

            
                

print(solution("  TRy HElLo  WORLD "))