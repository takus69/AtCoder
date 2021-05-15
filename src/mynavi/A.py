def run(A):
    ans = 'No'
    if A[0] - A[1] == A[1] - A[2]:
        ans = 'Yes'
    elif A[0] - A[2] == A[2] - A[1]:
        ans = 'Yes'
    elif A[1] - A[0] == A[0] - A[2]:
        ans = 'Yes'
    return ans


def main():
    A = list(map(int, input().split()))
    print(run(A))


if __name__ == '__main__':
    main()
