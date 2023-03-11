N = int(input())
A = list(map(int, input().split()))

c = {i+1: 0 for i in range(N)}

for i in range(N):
    if c[i+1] == 0:
        c[A[i]] = 1

X = []
for i in range(N):
    if c[i+1] == 0:
        X.append(i+1)

print(len(X))
print(' '.join(map(str, X)))
