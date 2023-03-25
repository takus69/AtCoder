n = int(input())
W = list(input().split())

ans = 'No'
for w in W:
    if  w == 'and' or w == 'not' or w == 'that' or w == 'the' or w == 'you':
        ans = 'Yes'
print(ans)
