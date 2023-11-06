from fractions import Fraction


def solution(N, stages):
    fail_rate = []
    answer = []
    for stage in range(1, N + 1):
        tried = len(tuple(filter(lambda x: x >= stage, stages)))
        failed = stages.count(stage)
        if tried != 0:
            fail_rate.append((Fraction(failed / tried), stage))
        else:
            fail_rate.append(0)
    fail_rate.sort(reverse=True, key=lambda x: x[0])
    for _, stage in fail_rate:
        answer.append(stage)
    return answer


print(solution(4, [4, 4, 4, 4, 4]))
