T = int(input())
for _ in range(T):
    N = int(input())
    i1 = []
    b = str(bin(N))[2:]
    n = len(b)
    #print('変換', b)
    cnt = 0
    ans = ''
    for i in range(n):
        if b[i] == '1':
            cnt += 1
            i1.append(i)

        if cnt > 3:
            ans += '0'
        else:
            ans += b[i]
    #print('対象', N, cnt, i1, n)
    if N < 7:
        print(-1)
    else:
        if cnt == 1 or (cnt == 2 and i1[1] >= n-2):
            ans = '0111' + '0'*(n-4)
        elif cnt == 2:
            ans = '1' + '0'*(i1[1]) + '11' + '0'*(n-i1[1]-3)
        #print('結果', '0b'+ans)
        print(int(ans, base=2))