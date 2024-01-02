b = list(map(int, input().split()))
a2b = {}
b2a = {}
for i in range(10):
    a2b[i] = b[i]
    b2a[b[i]] = i

N = int(input())
A = []
for _ in range(N):
    a = input()
    a2 = ''
    for s in a:
        a2 += str(b2a[int(s)])
    A.append(a2)
# print(a2b, b2a)
# print(A)
A = sorted(map(int, A))
A = list(map(str, A))
# print(A)
A2 = []
for a in A:
    a2 = ''
    for s in a:
        a2 += str(a2b[int(s)])
    A2.append(a2)

# print(A2)
for a in A2:
    print(a)
