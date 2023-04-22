N = int(input())

i = 0
j = N-1
si = 0
sj = 1
while True:
    m = (i+j)//2
    print('?', m+1)
    sm = int(input())
    # print(i, pre_i, si, pre_si)
    if m-i == 1 and sm != si:
        print('!', i+1)
        break
    elif j-m == 1 and sm != sj:
        print('!', m+1)
        break
    if sm == 0:
        i = m
        si = sm
    else:
        j = m
        sj = sm
