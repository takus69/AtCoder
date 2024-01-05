a, b, x = map(int, input().split())

if a%x==0:
    a2 = a
else:
    a2 = x + a - a%x
b2 = b - b%x
 
# print(a2, b2, x)
print((b2-a2)//x + 1)
