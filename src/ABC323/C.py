N, M = map(int, input().split())
A = list(map(int, input().split()))
score = {i:i+1 for i in range(N)}
S = []
for i in range(N):
    S.append(input())
    for j in range(M):
        if S[i][j] == 'o':
            score[i] += A[j]

max_score = max(score.values())
A2 = [(i, A[i]) for i in range(M)]
A2 = sorted(A2, key=lambda x:x[1], reverse=True)
for i in range(N):
    diff_score = max_score - score[i]
    # print(diff_score, max_score, score[i])
    cnt = 0
    if diff_score > 0:
        for j in range(M):
            a = A2[j][1]
            s = S[i][A2[j][0]]
            if s == 'x':
                diff_score -= a
                cnt += 1
            if diff_score < 0:
                break
        # print(diff_score, max_score, score[i])
    print(cnt)
