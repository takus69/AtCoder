mod = 1000000007


# 計算量O(m**0.5*nlog(mod))
def run(n, m):
    # print('{}を{}個の数列で表現'.format(m, n))
    ans = 1
    # 計算量O(m**0.5)
    for i in range(2, m):
        # iの2乗以上は素数は最大で1つしかない
        if i*i > m:
            break
        if m % i == 0:
            cnt = 0
            # 計算量O(logm)
            while m % i == 0:
                cnt += 1
                m //= i
            # 計算量O(nlog(mod))
            ans *= comb(cnt+n-1, n-1)
            ans %= mod
    # iの2乗以上の素数がある場合は、その配置の場合をかける
    if m != 1:
        ans *= n
        ans %= mod
    return ans


# 計算量O(nlog(mod))
def comb(n, r):
    if r > (n-r):
        r = n-r
    mul = 1
    div = 1
    # 計算量O(n)
    for i in range(r):
        mul *= n-i
        div *= i+1
        mul %= mod
        div %= mod
    mul %= mod
    div %= mod
    # 計算量O(log(mod))
    return (mul * modpow(div, (mod-2))) % mod


'''
def factorial(n):
    if n in fact:
        return fact[n]
    else:
        fact[n] = n*factorial(n-1)
        return fact[n]
'''


# 計算量O(log(p))
def modpow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        halfp = p // 2
        half = modpow(a, halfp)
        return int((half * half) % mod)
    else:
        return int((a * modpow(a, p-1)) % mod)


def main():
    n, m = map(int, input().split())
    print(run(n, m))


if __name__ == '__main__':
    main()
