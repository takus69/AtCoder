N = int(input())
cnt_AB = 0
cnt_A = 0  # 最後がA
cnt_B = 0  # 最初がB
cnt_BA = 0  # 最後がAかつ最初がB
for _ in range(N):
    s = input()
    if s.startswith('B'):
        cnt_B += 1
        if s.endswith('A'):
            cnt_BA += 1
    if s.endswith('A'):
        cnt_A += 1
    for i in range(len(s)-1):
        if s[i:i+2] == 'AB':
            cnt_AB += 1
ans = cnt_AB + min(cnt_A, cnt_B)
if cnt_BA != 0 and cnt_BA == cnt_B and cnt_BA == cnt_A:
    ans -= 1
print(ans)
