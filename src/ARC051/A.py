x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

# 赤の判定
if x1-r < x2 or x1+r > x3 or y1-r < y2 or y1+r > y3:
    print('YES')
else:
    print('NO')

# 青の判定
if (x1-x2)**2+(y1-y2)**2 > r**2 or (x1-x3)**2+(y1-y2)**2 > r**2 or (x1-x2)**2+(y1-y3)**2 > r**2 or (x1-x3)**2+(y1-y3)**2 > r**2:
    print('YES')
else:
    print('NO')
