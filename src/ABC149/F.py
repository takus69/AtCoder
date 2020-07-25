def run(N, E):
    '''
    各辺で木を分割し、1つの部分木頂点の数xを求める
    その辺がSに含まれる確率は(1-(1/2)^x)*(1-(1/2)^(N-x))となる
    各辺の和+1がSの頂点の個数の期待値になり
    求める答えは、(Sの頂点の個数の期待値) - (黒の頂点の個数の期待値=N/2)から求まる
    '''
    edge = {i: [] for i in range(N)}
    for a, b in E:
        edge[a].append(b)
        edge[b].append(a)
    a, b = E[0]
    visited = [True] + [False for _ in range(N)]
    dfs(v, edge, visited, False)

    return (N, E)


def dfs(v, edge, visited, is_b):
    visited[v] = True
    for v in edge[v]:
        if not visited[v]:
            if v == b:
                is_b = True
            dfs(v, edge, visited, is_b)


def main():
    N = int(input())
    E = []
    for _ in range(N-1):
        E.append(list(map(int, input().split())))
    print(run(N, E))


if __name__ == '__main__':
    main()
