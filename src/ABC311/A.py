N = int(input())
S = input()

fa = False
fb = False
fc = False
for i in range(len(S)):
    s = S[i]
    if s == 'A':
        fa = True
    elif s == 'B':
        fb = True
    else:
        fc = True
    if fa and fb and fc:
        print(i+1)
        break