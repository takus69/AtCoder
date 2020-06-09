N, M = map(int, input().split())
a = list(map(int, input().split()))

n_a = [0] * N
max_a = 0
min_a = 10**9
min_i = 1
ans = []


def get_index(n_a, ai):
    li = 0
    ri = N - 1
    # cnt = 0
    while li < ri:
        # cnt += 1
        # print(cnt)
        n_i = li + (ri - li + 1) // 2
        if n_a[n_i] >= ai:
            # print('loop', n_i, li, ri)
            li = n_i + 1
        else:
            ri = n_i
            if n_a[ri-1] < ai:
                ri -= 1
            else:
                li = ri
    return ri


for i in range(M):
    # print('M start:', M)
    ai = a[i]
    # print('aa', ai, max_a, min_a, min_i)
    if ai > max_a:
        n_a[0] = ai
        ans.append(1)
        max_a = ai
    elif ai > min_a:
        # print('get_index')
        n_i = get_index(n_a, ai)
        # print('get_index:', n_i)
        n_a[n_i] = ai
        ans.append(n_i+1)
    else:
        if min_i < N:
            n_a[min_i] = ai
            ans.append(min_i+1)
            min_i += 1
        else:
            ans.append(-1)
    min_a = n_a[min_i-1]
    # print('M end')
    # print(n_a)

for a in ans:
    print(a)
