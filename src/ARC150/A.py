import re


def check(S, K):
    p = '[0?][1?]{' + str(K) + '}[0?]'
    results = re.findall(p, S)
    p = '^[1?]{' + str(K) + '}[0?]'
    results += re.findall(p, S)
    p = '[0?][1?]{' + str(K) + '}$'
    results += re.findall(p, S)
    p = '^[1?]{' + str(K) + '}$'
    results += re.findall(p, S)

    print(S, K, results)

    if len(results) == 1:
        ret = 'Yes'
    else:
        ret = 'No'
    return ret


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        S = input()
    print(check(S, K))
    print(N, K, S)
