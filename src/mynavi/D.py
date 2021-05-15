def run(H, W, A):
    '''
    dp[i,j]をその地点から開始した際の最適解の点数(高橋君-青木君)とする
    高橋君はi+jが偶数の際に手番で、(i,j+1),(i+1,j)から最大化するように行動する
    青木君はi+jが奇数の際に手番で、(i,j+1),(i+1,j)から最小化するように行動する
    '''
    #dp = {}
    #dp[(H-1, W-1)] = 0
    dp = [[0]*W]*H
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            p1 = None
            p2 = None
            if i == H-1 and j == W-1:
                continue
            p = 1 + (-2)*((i+j)%2)
            if j+1 < W:
                if A[i][j+1] == '+':
                    #p1 = dp[(i,j+1)] + p
                    p1 = dp[i][j+1] + p
                else:
                    # p1 = dp[(i,j+1)] - p
                    p1 = dp[i][j+1] - p
            if i+1 < H:
                if A[i+1][j] == '+':
                    # p2 = dp[(i+1,j)] + p
                    p2 = dp[i+1][j] + p
                else:
                    # p2 = dp[(i+1,j)] - p
                    p2 = dp[i+1][j] - p
            if (i+j)%2 == 0:
                if p1 is None:
                    p1 = -10000
                if p2 is None:
                    p2 = -10000
                # dp[(i,j)] = max(p1, p2)
                dp[i][j] = max(p1, p2)
            else:
                if p1 is None:
                    p1 = 10000
                if p2 is None:
                    p2 = 10000
                # dp[(i,j)] = min(p1, p2)
                dp[i][j] = min(p1, p2)
    # print(dp)
    # if dp[(0,0)] > 0:
    if dp[0][0] > 0:
        ans = 'Takahashi'
    # elif dp[(0,0)] < 0:
    elif dp[0][0] < 0:
        ans = 'Aoki'
    else:
        ans = 'Draw'
    return ans

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(input())
    print(run(H, W, A))


if __name__ == '__main__':
    main()
