def compressing(s, cut):
    if len(s) < cut or not s[0:cut] == s[cut:cut * 2]:
        return 1
    elif s[0:cut] == s[cut:cut * 2]:
        return 1 + compressing(s[cut:], cut)

def solution(s):
    original_s = s
    compressed = [s]
    for cut in range(1, int(len(original_s)/2) + 1):
        s = original_s
        temp = ''
        while True:
            repeat = compressing(s, cut)
            temp = temp + str('' if repeat == 1 else repeat) + s[0:cut]
            s = s[cut * repeat:]
            if len(s) < cut:
                temp += s
                break
        compressed.append(temp)
    compressed.sort(key = len, reverse = True)
    return len(compressed.pop())
        
        
print(solution("xababcdcdababcdcd"))