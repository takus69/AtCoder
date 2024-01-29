import math

A, B, C = map(int, input().split())

max_t = (100 + B) / A
min_t = (100 - B) / A
d = 10**(-6)

def f(t):
    return A*t + B*math.sin(C*t*math.pi)

t_s = min_t
t_e = max_t
while True:
    t_m = (t_e + t_s)/2
    if abs(f(t_m) - 100) < d:
        break
    if f(t_m) < 100:
        t_s = t_m
    else:
        t_e = t_m

print(t_m)
