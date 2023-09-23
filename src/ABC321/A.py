N = input()

ans = 'Yes'
for i in range(len(N)-1):
    if int(N[i]) <= int(N[i+1]):
        ans = 'No'

print(ans)
