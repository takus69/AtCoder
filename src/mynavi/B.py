def run(N, S, T):
    No1S = S[0]
    No1T = T[0]
    No2T = 0
    for i in range(1, N):
        if No1T < T[i]:
            ans = No1S
            No2T = No1T
            No1S = S[i]
            No1T = T[i]
        elif No2T < T[i]:
            ans = S[i]
            No2T = T[i]
    return ans

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    print(run(N, S, T))


if __name__ == '__main__':
    main()
