N = int(input())
a = list(map(int, input().split()))

a = sorted(a)
ans = 0
stock = {}
for ai in a:
    stock[ai] = stock.get(ai, 0)+1
keys = sorted(list(stock.keys()))
r = len(keys)-1
stocks = 0
for k, v in stock.items():
    stocks += v-1
    stock[k] = 1
for i in range(1, N+1):
    # print(i, stock, stocks, keys)
    # 持っているか
    if i in stock.keys():
        if stock[i] > 0:
            ans = i
            stocks += stock[i]-1  # 同じ巻がある場合は売るためにストックしておく
            stock[i] = 0
            continue
    # 持っていないため買う
    sell_cnt = 2
    # 前の巻の余りから売る
    while sell_cnt > 0:
        if stocks > 0:
            stocks -= 1
            sell_cnt -= 1
        else:
            break
    if sell_cnt == 0:
        ans = i
        continue
    # 足りない分は後ろの巻から売る
    while sell_cnt > 0:
        if stock[keys[r]] == 0:
            r -= 1
            if r < 0:
                break
            else:
                if stock[keys[r]] == 0:
                    break
        if stock[keys[r]] > 0:
            sell_cnt -= 1
            stock[keys[r]] -= 1
    if sell_cnt == 0:
        ans = i
    else:
        break
print(ans)
