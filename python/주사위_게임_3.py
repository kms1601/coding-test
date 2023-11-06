def solution(a, b, c, d):
    dice = [0 for _ in range(7)]
    dice[a] += 1
    dice[b] += 1
    dice[c] += 1
    dice[d] += 1

    if 4 in dice:
        return dice.index(4) * 1111
    elif 3 in dice:
        p = dice.index(3)
        q = dice.index(1)
        return (10 * p + q) ** 2
    elif 2 in dice:
        if 1 in dice:
            qr = []
            for idx, num in enumerate(dice):
                if num == 1:
                    qr.append(idx)
            return qr[0] * qr[1]
        else:
            pq = []
            for idx, num in enumerate(dice):
                if num == 2:
                    pq.append(idx)
            return (pq[0] + pq[1]) * abs(pq[0] - pq[1])
    else:
        return dice.index(1)
