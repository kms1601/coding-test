def solution(survey, choices):
    answer = []
    score = {
        "RT": {"R": 0, "T": 0},
        "CF": {"C": 0, "F": 0},
        "JM": {"J": 0, "M": 0},
        "AN": {"A": 0, "N": 0},
    }
    change_cat = {"TR": "RT", "FC": "CF", "MJ": "JM", "NA": "AN"}
    change_val = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}

    for cat, cho in zip(survey, choices):
        if cat in change_cat:
            cat = change_cat[cat]
            cho = change_val[cho]
        if cho >= 4:
            score[cat][cat[0]] += cho - 4
        else:
            score[cat][cat[1]] += 4 - cho

    for cat in score:
        if score[cat][cat[0]] <= score[cat][cat[1]]:
            answer.append(cat[0])
        else:
            answer.append(cat[1])
    return "".join(answer)


print(solution(["TR", "RT", "TR"], [7, 1, 3]))
