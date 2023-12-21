from sortedcontainers import SortedList

Q = int(input())
s = SortedList([])
add = 0
for _ in range(Q):
    query = input()
    if query == '3':
        print(s.pop(0) + add)
    else:
        q, x = map(int, query.split())
        if q == 1:
            s.add((x - add))
        else:
            add += x
