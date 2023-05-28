N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
cnt = {}
now =''
for a in A:
    cnt[a] = cnt.get(a, 0) + 1
    now = a

ans = 'Yes'
#print(cnt.items())
for k, v in cnt.items():
    #print(k, v, A[0])
    if k == A[0]:
        if v > (N+1)/2:
            ans = 'No'
    else:
        if v >= (N+1)/2:
            ans = 'No'
    
print(ans)
