from itertools import permutations

def is_same(user, banned):
    if not len(user) == len(banned): return False
    same = 0
    for i in range(len(banned)):
        if user[i] == banned[i] or banned[i] == '*': same += 1
        else: break
    if same == len(user): return True
    else: return False

def solution(user_id, banned_id):
    answer = set()
    for i in permutations(user_id, len(banned_id)):
        count = 0
        for j in range(len(banned_id)):
            if is_same(i[j], banned_id[j]):
                count += 1
        if count == len(banned_id):
            answer.add(''.join(sorted(i)))
    print(answer)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))