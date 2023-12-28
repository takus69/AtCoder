import math

N = int(input())
x0, y0 = map(int, input().split())
xn_2, yn_2 = map(int, input().split())

'''
中心(xc, yc) = ((x0+xn_2)/2, (y0+yn_2)/2)
ベクトル(x0-xc, y0-yc)を2π/nだけ反時計回りに回転させる(ベクトルvとする)
(x1, y1) = (xc, yc) + v
回転行列以下の回転行列をかける
cosΘ, -sinΘ
sinΘ, cosΘ
'''

xc, yc = (x0+xn_2)/2, (y0+yn_2)/2
theta = 2*math.pi/N
x1 = xc + math.cos(theta)*(x0-xc) - math.sin(theta)*(y0-yc)
y1 = yc + math.sin(theta)*(x0-xc) + math.cos(theta)*(y0-yc)

print(f'{x1} {y1}')
