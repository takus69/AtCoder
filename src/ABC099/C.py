def run(n):
    cost = [6**i for i in range(7)]
    cost.extend([9**i for i in range(1, 6)])
    cost = sorted(cost)
    # print(cost)
    
    dp = {0: 0}
    for i in range(1, n+1):
        dp[i] = dp[i-1] + 1
        for c in cost:
            if i >= c:
                dp[i] = min(dp[i-c]+1, dp[i])
            else:
                break
        # print(i, dp[i])
    return dp[n]


def main():
    n = int(input())
    print(run(n))


if __name__ == '__main__':
    main()
