N, M, H, K = map(int, input().split())
S = input()
xy = {}
for _ in range(M):
    x, y = map(int, input().split())
    xy[(x, y)] = 1
# print(xy)

ans = 'Yes'
x, y = 0, 0
for i in range(len(S)):
    s = S[i]
    if s == 'R':
        x += 1
    elif s == 'L':
        x -= 1
    elif s == 'U':
        y += 1
    else:
        y -= 1
    H -= 1
    # print((x, y), H, s)
    if H < 0:
        ans = 'No'
        break
    if xy.get((x, y), 0) == 1 and H < K:
        xy[(x, y)] = 0
        H = K

print(ans)
