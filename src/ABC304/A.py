N = int(input())
S = []
A = []
start_i = 0
age = 10**10
for i in range(N):
    s, a = input().split()
    a = int(a)
    S.append(s)
    A.append(a)
    if age > a:
        age = a
        start_i = i

for i in range(N):
    print(S[(i+start_i)%N])