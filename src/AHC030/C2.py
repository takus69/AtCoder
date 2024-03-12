# read prior information
line = input().split()
N = int(line[0])
M = int(line[1])
eps = float(line[2])
fields = []
all_d = 0
for _ in range(M):
    line = input().split()
    all_d += int(line[0])
    ps = []
    for i in range(int(line[0])):
        ps.append((int(line[2*i+1]), int(line[2*i+2])))
    fields.append(ps)

# drill every square
cnt = 0
has_oil = []
for i in range(N):
    if all_d == cnt:
        break
    for j in range(N):
        if all_d == cnt:
            break
        print("q 1 {} {}".format(i, j))
        resp = input()
        cnt += int(resp)
        if resp != "0":
            has_oil.append((i, j))

print("a {} {}".format(len(has_oil), ' '.join(map(lambda x: "{} {}".format(x[0], x[1]), has_oil))))
resp = input()
assert resp == "1"
