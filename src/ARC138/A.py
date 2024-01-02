N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted([(i, A[i]) for i in range(N)], key=lambda x: (x[1], -x[0]))
max_i = -1
ans = -1
for ai, a in A:
    # print(ai, a, max_i)
    if ai >= K:
        if max_i > -1:
            if ans == -1 or ans > ai - max_i:
                ans = ai - max_i
    else:
        if max_i < ai:
            max_i = ai
print(ans)
