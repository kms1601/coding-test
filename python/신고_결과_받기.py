from collections import defaultdict


def solution(id_list, report, k):
    data = {i: {"history": defaultdict(int), "reported": 0} for i in id_list}
    ban_list = []
    mailing_cnt = [0 for _ in range(len(id_list))]
    for rep in report:
        reporter, target = rep.split()
        if not data[reporter]["history"][target]:
            data[target]["reported"] += 1
            data[reporter]["history"][target] = 1
    for id in id_list:
        if data[id]["reported"] >= k:
            ban_list.append(id)
    for ban in ban_list:
        for idx, id in enumerate(id_list):
            if data[id]["history"][ban]:
                mailing_cnt[idx] += 1
    return mailing_cnt


print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
