import collections

S = input()

d = collections.Counter(S)
d = sorted(d.items(), key=lambda x: x[0])
d = sorted(d, key=lambda x: x[1], reverse=True)
# print(d)
print(d[0][0])
