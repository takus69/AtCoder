import fractions
import math


def run(n, m, s, t):
    ret = -1
    if s[0] != t[0]:
        return ret
    g = fractions.gcd(n, m)
    if g == 1:
        big = max([n, m])
        small = min([n, m])
        if small == 1:
            for i in range(math.sqrt(n)):
                if big % i == 0:
                    return i
        else:
            return n*m
    n_s = n//g
    m_s = m//g
    mn = n_s * m_s
    small = min([g, mn])
    for j in range(1, g+1):
        if n_s * m_s < j:
            return -1
        n_eval = j*n_s
        m_eval = j*m_s
        eval = True
        for i in range(1, g):
            if i*n_eval >= n:
                eval = False
                continue
            if i*m_eval >= m:
                eval = False
                continue
            if s[i*n_eval] != t[i*m_eval]:
                eval = False
                continue
        if eval:
            return n_eval * m_eval * g
    return -1


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    print(run(n, m, s, t))


if __name__ == '__main__':
    main()
