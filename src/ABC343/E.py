V = list(map(int, input().split()))

def f(a, b, c):
    l = max(a, b, c)
    r = min(a, b, c)+7
    if l > r:
        return 0
    else:
        return r-l
    
def g(a, b):
    l = max(a, b)
    r = min(a, b)+7
    if l > r:
        return 0
    else:
        return r-l
a1, b1, c1, a2, b2, c2, a3, b3, c3 = 0, 0, 0, 0, 1, 7, -5, 1, 0
if V[0] + V[1]*2 + V[2]*3 != (7**3)*3:
    print('No')
else:
    a1, b1, c1 = 0, 0, 0
    ans = 'No'
    for a2 in range(-1, 8):
        if ans == 'Yes':
            break
        for b2 in range(-1, 8):
            if ans == 'Yes':
                break
            for c2 in range(-1, 8):
                if ans == 'Yes':
                    break
                for a3 in range(-7, 8):
                    if ans == 'Yes':
                        break
                    for b3 in range(-7, 8):
                        if ans == 'Yes':
                            break
                        for c3 in range(-7, 8):
                            # V3
                            v3 = f(a1, a2, a3)*f(b1, b2, b3)*f(c1, c2, c3)
                            if v3 != V[2]:
                                continue
                            # print('v3', v3, a1, b1, c1, a2, b2, c2, a3, b3, c3)
                            
                            # V2
                            v2 = g(a1, a2)*g(b1, b2)*g(c1, c2) + g(a2, a3)*g(b2, b3)*g(c2, c3) + g(a3, a1)*g(b3, b1)*g(c3, c1) - v3*3
                            if v2 != V[1]:
                                continue
                            # print('v2', v2, a1, b1, c1, a2, b2, c2, a3, b3, c3)

                            # V1
                            v1 = 7*7*7*3 - v2*2 - v3*3
                            if v1 != V[0]:
                                continue

                            ans = 'Yes'
                            print(ans)
                            print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
                            break

    if ans != 'Yes':
        print(ans)
