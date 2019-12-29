def run(x):
    n = 10**5 + 1000
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    for i in range(x, n):
        if is_prime[i]:
            ans = i
            break
    return ans


def main():
    x = int(input())
    print(run(x))


if __name__ == '__main__':
    main()
