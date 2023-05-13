N = int(input())
A = list(map(int, input().split()))

ans = [A[0]]

for a in A[1:]:
    sa = ans[-1]
    if a > sa:
        # print('add', [i for i in range(sa+1, a+1)])
        ans += [i for i in range(sa+1, a+1)]
    else:
        ans += [i for i in range(sa-1, a-1, -1)]
        # print('add', [i for i in range(sa-1, a-1, -1)])
    # print(ans)

ans = list(map(str, ans))
print(' '.join(ans))
