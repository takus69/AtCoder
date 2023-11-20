N = int(input())
A = list(map(int, input().split()))

'''
grundy数=Ai mod(k+1)
素のAでgrundy数を求めて、非ゼロならkの最大値はない(-1)
素のAでgrundy数を求めて、ゼロなら以下
  k=max(A)-1にするとgrundy数が変わるので、非ゼロになりk=max(A)-1が答え(max(A)-1)
  ただし、Aの同じ数字がすべて偶数の組の場合は常にgrundy数が0となるため必勝法はない(0)
'''

A = sorted(A)
dic_A = {}
for a in A:
    dic_A[a] = dic_A.get(a, 0) + 1
A = []
for k, v in dic_A.items():
    if v % 2 == 1:
        A.append(k)

g = 0
for a in A:
    g ^= a
if len(A) == 0:
    ans = 0
elif g != 0:
    ans = -1
else:
    ans = max(A) - 1

print(ans)
