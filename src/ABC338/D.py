N, M = map(int, input().split())
X = list(map(int, input().split()))

# N=>1が封鎖を計算する(計算しやすい)
v = [0] * (N+1)
for i in range(M-1):
    l, r = min(X[i], X[i+1]), max(X[i], X[i+1])
    dis = r - l
    v[1] += dis  # N=>1が封鎖を計算(後ろの計算で、1=>2封鎖の考慮がされ、最終的に1=>2封鎖)
    v[l] += (N-dis) - dis  # 封鎖する橋がl=>rの時は逆転
    v[r] += dis - (N-dis)  # 封鎖する島がl=>rから抜けたとき元に戻す
dis = v[1]
ans = dis
for i in range(2, N+1):
    dis += v[i]
    ans = min(ans, dis)
print(ans)
