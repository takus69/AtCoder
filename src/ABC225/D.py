N, Q = map(int, input().split())
train = {}
train2 = {}
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1], q[2]
        train[x] = (y, True)
        train2[y] = (x, True)
    elif q[0] == 2:
        x, y = q[1], q[2]
        train[x] = (y, False)
        train2[y] = (x, False)
    else:
        x = q[1]
        ans = []
        cnt = 0
        if x in train2.keys():
            while train2[x][1]:
                x = train2[x][0]
                if x not in train2.keys():
                    break
        ans.append(x)
        cnt += 1
        if x in train.keys():
            while train[x][1]:
                x = train[x][0]
                ans.append(x)
                cnt += 1
                if x not in train.keys():
                    break
        print(f'{cnt} ' + ' '.join(map(str, ans)))
