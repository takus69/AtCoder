N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

# A(i-1)の次が+か-である組み合わせの個数
# A(i-1)の出現する総数を合わせるため、dp[(i, '+')]は2**(N-i)、dp[(i, '-')]は2**(N-i-1)倍する
dp = {(0, '+'): 1, (0, '-'): 0}
dp_sum = {(0, '+'): A[0], (0, '-'): 0}
for i in range(N-1):
    dp[(i+1, '+')] = dp[(i, '+')] + dp[(i, '-')]
    dp[(i+1, '-')] = dp[(i, '+')]
    dp_sum[(i+1, '+')] = dp_sum[(i, '+')] + dp_sum[(i, '-')] + A[i+1]*dp[(i+1), '+']
    dp_sum[(i+1, '-')] = dp_sum[(i, '+')] - A[i+1]*dp[(i+1), '-']
    dp_sum[(i+1, '+')] %= MOD
    dp_sum[(i+1, '-')] %= MOD

ans = dp_sum[(N-1, '+')] + dp_sum[(N-1, '-')]
ans %= MOD

print(ans)
