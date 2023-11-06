def solution(word):
    answer = 0
    preset = {'A' : [1, 1, 1, 1, 1], 'E' : [782, 157, 32, 7, 2], 'I' : [1563, 313, 63, 13, 3], 'O' : [2344, 469, 94, 19, 4], 'U' : [3125, 625, 125, 25, 5]}
    for index, vowel in enumerate(word):
        answer += preset[vowel][index]
    return answer

print(solution('AAAE'))