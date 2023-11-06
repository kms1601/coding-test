n = int(input())
len_ = int(input())
str_ = input()
pn = "I" + "OI" * n
idx = 0
answer = 0
while idx < len_:
    if str_[idx:2 * n + 1 + idx] == pn:
        answer += 1
        idx += 3
    else:
        idx += 1
print(answer)
