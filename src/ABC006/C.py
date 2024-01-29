N, M = map(int, input().split())

if M-2*N >= 0:
    a3 = (M-2*N)//2
    a2 = (M-2*N)%2
else:
    a3 = -1
    a2 = -1
a1 = N-a2-a3
if a1 < 0 or a3 < 0:
    a1, a2, a3 = -1, -1, -1
# print(a1+a2+a3, 2*a1+3*a2+4*a3)
print(a1, a2, a3)
