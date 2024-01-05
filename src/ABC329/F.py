N, Q = map(int, input().split())
C = list(map(int, input().split()))
box = {i+1: set([C[i]]) for i in range(N)}

for _ in range(Q):
    a, b = map(int, input().split())
    box_a = box[a]
    box_b = box[b]
    if len(box_a) <= len(box_b):
        for c in box_a:
            box_b.add(c)
    else:
        for c in box_b:
            box_a.add(c)
        box_b = box_a
    box[a] = set([])
    box[b] = box_b
    print(len(box_b))
