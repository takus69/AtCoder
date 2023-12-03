Na, Nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
C = set(A+B)

cnt_and = 0
cnt_or = len(C)

i = 0
B_cnt = len(B)
for a in A:
    while i < B_cnt:
        if B[i] == a:
            cnt_and += 1
            i += 1
            break
        elif B[i] < a:
            i += 1
        else:
            break

print(cnt_and/cnt_or)
