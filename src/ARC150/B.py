T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    if B <= A:
        ret = A - B
    else:
        ret = ((B//A)+1)*A - B
        mm = B % A
        ss = B // A
        for X in range(min(A-mm, abs((B//ss)-A))):
            m = B % (A+X)
            if m == 0:
                Y = 0
            else:
                Y = (A+X) - m
            ret = min(ret, X+Y)
    # print(A, B, m, )
    # print('*** ans ***')
    print(ret)