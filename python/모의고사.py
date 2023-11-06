def score(answers, marking):
    marking_all = []
    score = 0
    while not len(answers) == len(marking_all):
        if len(answers) > len(marking_all):
            marking_all.extend(marking)
        elif len(answers) < len(marking_all):
            marking_all = marking_all[:len(answers)]
    for index, mark in enumerate(marking_all):
        if mark == answers[index]:
            score += 1
    return score
        
def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_list = [[1, score(answers, A)], [2, score(answers, B)], [3, score(answers, C)]] 
    for i in score_list:
        if i[1] == max([i[1] for i in score_list]):
            answer.append(i[0])
    return answer
    
   
print(solution([1,3,2,4,2]))
        