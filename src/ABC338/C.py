N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
x, y = 0, 0
for tmp_x in range(max(Q)+1):
    tmp_y = 10**6
    for i in range(N):
        if tmp_x * A[i] > Q[i]:
            tmp_x = -10**6
            break
        if B[i] == 0:
            continue
        else:
            tmp_y = min((Q[i] - (A[i]*tmp_x))//B[i], tmp_y)
        # print(ans, tmp_x, tmp_y)
    ans = max(tmp_x + tmp_y, ans)

print(ans)
