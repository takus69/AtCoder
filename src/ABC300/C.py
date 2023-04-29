H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))

N = min(H, W)
S = [0]*N

for a in range(H):
    for b in range(W):
        n = -1
        if C[a][b] == '#':
            for i in range(N):
                try:
                    if C[a+i+1][b+i+1] == C[a+i+1][b-i-1] == C[a-i-1][b+i+1] == C[a-i-1][b-i-1] == '#':
                        n += 1
                    else:
                        if n > -1:
                            S[n] += 1
                        break
                except:
                    if n > -1:
                        S[n] += 1
                    break

print(' '.join(map(str, S)))
