N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

queue = [[1,1]]
starts = {(1,1): 1}
can = [[0]*M for _ in range(N)]
can[1][1] = 1
i = 0

while len(queue) > i:
    #if i > 3:
    #    break
    now = queue[i]
    move = (now[0], now[1])
    # 右移動
    for j in range(now[1]+1, M):
        if S[move[0]][j] == '#':
            if move in starts.keys():
                None
            else:
                queue.append(move)
                starts[move] = 1
            break
        else:
            move = (move[0], j)
            can[move[0]][move[1]] = 1
    # 左移動
    move = (now[0], now[1])
    for j in range(now[1]-1, -1, -1):
        if S[move[0]][j] == '#':
            if move in starts.keys():
                None
            else:
                queue.append(move)
                starts[move] = 1
            break
        else:
            move = (move[0], j)
            can[move[0]][move[1]] = 1
    # 上移動
    move = (now[0], now[1])
    for j in range(now[0]-1, -1, -1):
        if S[j][move[1]] == '#':
            if move in starts.keys():
                None
            else:
                queue.append(move)
                starts[move] = 1
            break
        else:
            move = (j, move[1])
            can[move[0]][move[1]] = 1
    # 下移動
    move = (now[0], now[1])
    for j in range(now[0]+1, N):
        #print(i, j, S[j][move[1]], move[1], now, move)
        if S[j][move[1]] == '#':
            if move in starts.keys():
                None
            else:
                queue.append(move)
                starts[move] = 1
            break
        else:
            move = (j, move[1])
            can[move[0]][move[1]] = 1
    i += 1

ans = 0
#show = []
#for _ in range(N):
#    show.append([])
for i in range(N):
    for j in range(M):
        if can[i][j] == 1 and S[i][j] == '.':
            ans += 1
            #show[i].append('o')
        #else:
            #show[i].append(S[i][j])
print(ans)
#for s in show:
#    print(''.join(s))
#print(queue[:6])