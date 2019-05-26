def run(N, lists):
    sorted_items = sorted(
        lists,
        key=lambda x: (x['P']),
        reverse=True
    )
    sorted_items = sorted(
        sorted_items,
        key=lambda x: (x['S']),
    )
    return sorted_items


def main():
    N = int(input())
    lists = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        lists.append({'id': i+1, 'S': S, 'P': P})
    sorted_lists = run(N, lists)
    for item in sorted_lists:
        print(item['id'])


if __name__ == '__main__':
    main()
