N = int(input())
P = list(map(int, input().split()))
data = []

for i in range(N):
    data.append([i+1, P[i]])

diff2 = []
for i in range(N-1):
    d1 = data[i]
    d2 = data[i+1]
    diff2.append(abs(d1[0]-d2[0])+abs(d1[1]-d2[1]))
D3 = [diff2[0]]
for i in range(len(diff2)-1):
    D3.append(min(diff2[i], diff2[i+1]))
D3.append(diff2[-1])

data = sorted(data, key=lambda x:x[1])
diff = []
for i in range(N-1):
    d1 = data[i]
    d2 = data[i+1]
    #print('d1:', d1, 'd2:', d2)
    diff.append(abs(d1[0]-d2[0])+abs(d1[1]-d2[1]))

D = [diff[0]]
for i in range(len(diff)-1):
    D.append(min(diff[i], diff[i+1]))
D.append(diff[-1])

D2 = []
for i in range(len(data)):
    j = data[i][0]-1
    D2.append([j, D[i]])
#print('D2:', D2)
D2 = sorted(D2, key=lambda x:x[0])
#print('D2:', D2)
ret = ''
for i in range(N):
    ret += str(min(D2[i][1], D3[i])) + ' '
#print('data:', data)
#print('diff:', diff)
#print('D2:', D2)
#print('D3:', D3)
print(ret[:-1])
