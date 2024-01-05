N = int(input())
xyh = []
for _ in range(N):
    xyh.append(list(map(int, input().split())))
xyh = sorted(xyh, key=lambda x: x[2], reverse=True)
# print(xyh)
for cx in range(101):
    for cy in range(101):
        ch = None
        flg = True
        for x, y, h in xyh:
            tmp_h = h + abs(cx-x) + abs(cy-y)
            # print(cx, cy, tmp_h, x, y, h)
            if ch is None:
                ch = tmp_h
            if h == 0:
                if ch > tmp_h:
                    flg = False
                    break
            else:
                if ch != tmp_h:
                    flg = False
                    # print(1, ch, tmp_h, flg)
                    break
        if flg:
            # print(2, ch, tmp_h, flg)
            break
    if flg:
        # print(3, ch, tmp_h, flg)
        break
print(cx, cy, ch)

