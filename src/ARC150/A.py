T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = input()

    # jからj+K-1に0がない
    # j-1までとj+K以降に1がない
    cnt0 = [0]
    cnt1 = [0]
    for s in S:
        if s == '0':
            cnt0.append(cnt0[-1]+1)
        else:
            cnt0.append(cnt0[-1])
        if s == '1':
            cnt1.append(cnt1[-1]+1)
        else:
            cnt1.append(cnt1[-1])
    num = 0
    for j in range(1, N-K+2):
        # print(len(cnt0), 'j:', j, j+K, cnt0[j+K-1])
        # print('j:', j, 'num:', num, cnt0, cnt1)
        if cnt1[j-1] == 0 and cnt1[j+K-1] == cnt1[-1] and cnt0[j-1] == cnt0[j+K-1]:
            num += 1
    if num == 1:
        print('Yes')
    else:
        print('No')
