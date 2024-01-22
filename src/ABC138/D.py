N, Q = map(int, input().split())
ab = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)
px = {i: 0 for i in range(1, N+1)}
for _ in range(Q):
    p, x = map(int, input().split())
    px[p] += x

import sys
sys.setrecursionlimit(10**6)

ans = [0 for _ in range(N)]
def dfs(p, E, S):
    '''
    p: 深さ優先探索を開始する頂点
    E: pに繋がっている辺の配列
    S: 訪問済みかのフラグ
    '''
    # メイン処理を書く
    ans[p-1] += px[p]
    for p2 in E[p]:
        if not S[p2]:
            S[p2] = True
            # 前処理を書く
            ans[p2-1] += ans[p-1]
            dfs(p2, E, S)
            # 後処理を書く

S = [False for _ in range(N+1)]
S[1] = True
dfs(1, ab, S)

print(' '.join(map(str, ans)))
