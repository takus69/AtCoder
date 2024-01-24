d = {
    'b': 1, 'c': 1, 'B': 1, 'C': 1,
    'd': 2, 'w': 2, 'D': 2, 'W': 2,
    't': 3, 'j': 3, 'T': 3, 'J': 3,
    'f': 4, 'q': 4, 'F': 4, 'Q': 4,
    'l': 5, 'v': 5, 'L': 5, 'V': 5,
    's': 6, 'x': 6, 'S': 6, 'X': 6,
    'p': 7, 'm': 7, 'P': 7, 'M': 7,
    'h': 8, 'k': 8, 'H': 8, 'K': 8,
    'n': 9, 'g': 9, 'N': 9, 'G': 9,
    'z': 0, 'r': 0, 'Z': 0, 'R': 0,
}

N = int(input())
w = list(input().split())

ans = ''
for wi in w:
    tmp = ''
    for c in wi:
        if c in d.keys():
            tmp += str(d[c])
    if tmp != '':
        ans += ' ' + tmp

print(ans[1:])
