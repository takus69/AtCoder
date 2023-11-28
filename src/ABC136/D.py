S = input()

'''
RLのところに最後は固まる
RLに偶数で移動できるところに最終はなる
'''

N = len(S)
ans = [0] * N
cnt = 0
for i in range(N-1):
    if S[i] == 'R':
        cnt += 1
        if S[i+1] == 'L':
            ans[i] += cnt//2 + cnt%2
            ans[i+1] += cnt//2
            cnt = 0
for i in range(N-1, 0, -1):
    if S[i] == 'L':
        cnt += 1
        if S[i-1] == 'R':
            ans[i] += cnt//2 + cnt%2
            ans[i-1] += cnt//2
            cnt = 0
print(' '.join(map(str, ans)))
