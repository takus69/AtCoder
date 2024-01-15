N, K = map(int, input().split())

ans = 0
ans += 6*(K-1)*(N-K)
ans += 1
ans += 3*(N-K)
ans += 3*(K-1)
ans /= N**3
print(ans)
