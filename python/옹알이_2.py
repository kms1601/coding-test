def solution(babbling):
    cnt = 0
    for word in babbling:
        passed = True
        last = ""
        while word:
            if word[:2] != last and word[:2] in ["ye", "ma"]:
                last = word[:2]
                word = word[2:]
            elif word[:3] != last and word[:3] in ["aya", "woo"]:
                last = word[:3]
                word = word[3:]
            else:
                passed = False
                break
        if passed:
            cnt += 1
    return cnt


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
