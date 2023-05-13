N = int(input())
S = input()

nt = 0
na = 0

nc = N//2 + N%2
ans = 'S'

for i in range(N):
    if S[i] == 'T':
        nt += 1
    else:
        na += 1
    if nt >= nc:
        ans = 'T'
        break
    elif na >= nc:
        ans = 'A'
        break

print(ans)