def solution(lottos, win_nums):
    correct = 0
    zero = 0
    for num in lottos:
        if num in win_nums:
            correct += 1
        elif num == 0:
            zero += 1
    min_ = 7 - correct
    max_ = 7 - (correct + zero)
    
    return [max_ if max_ != 7 else 6, min_ if min_ != 7 else 6]
