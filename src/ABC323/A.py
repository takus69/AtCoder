S = input()

ans = 'Yes'
for i in range(1, 16, 2):
    # print(i, S[i])
    if S[i] == '1':
        ans = 'No'
print(ans)
