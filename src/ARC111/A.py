import math

N, M = map(int, input().split())

# M**2で割った余りを求める
tmp2 = pow(10, N, M**2)

ans = (tmp2//M)%M
# print(ans)
'''
10^N = Ma1+b1
a1 = Ma2+b2
10^N = M^2*a2+M*b2+b1
M*b2 = (10^N-M^2*a2)-b1
10^N-M^2*a2 = 10^N(mod M**2)
b1 = 10^N(mod M)
b2 = (10^N(mod M**2) - 10^N(mod M))/M
'''
tmp = pow(10, N, M)
tmp2 = pow(10, N, M**2)
print((tmp2-tmp)//M)
