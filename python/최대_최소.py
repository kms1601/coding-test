from math import gcd

def solution(n, m):
    gcd_ = gcd(n, m)
    return [gcd_, n * m / gcd_]
