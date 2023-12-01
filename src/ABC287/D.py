S = input()
T = input()

head = [1]  # 先頭からi番目がTと一致していたら1, 一致していなかったら0
tail = [1]  # 後方からi番目がTと一致していたら1, 一致していなかったら0
n = len(T)

for i in range(n):
    s = S[i]
    t = T[i]
    h = head[-1]
    if (s == t or s == '?' or t == '?') and h == 1:
        head.append(1)
    else:
        head.append(0)

for i in range(n):
    s = S[-i-1]
    t = T[-i-1]
    h = tail[-1]
    if (s == t or s == '?' or t == '?') and h == 1:
        tail.append(1)
    else:
        tail.append(0)
# print(head, tail)
for i in range(n+1):
    if head[i] == 1 and tail[-i-1] == 1:
        print('Yes')
    else:
        print('No')
