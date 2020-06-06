N, M, Q = map(int, input().split())

scores = [N] * M
passes = {i: [] for i in range(N)}
ans = []

# print('score:', scores)
# print('passes:', passes)


def sum_scores(n):
    ans = 0
    for i in passes[n]:
        ans += scores[i]
    return ans


for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        n = s[1] - 1
        ans.append(sum_scores(n))
        # print(ans)
    else:
        n = s[1] - 1
        m = s[2] - 1
        passes[n].append(m)
        scores[m] -= 1
        # print('score:', scores)
        # print('passes:', passes)

for a in ans:
    print(a)
