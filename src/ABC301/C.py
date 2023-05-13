S = input()
T = input()

dic_s = {}
dic_t = {}

ans = 'Yes'
target = ('a', 't', 'c', 'o', 'd', 'e', 'r')

for s in S:
    dic_s[s] = dic_s.get(s, 0) + 1

for t in T:
    dic_t[t] = dic_t.get(t, 0) + 1

# print(dic_s)
# print(dic_t)

for k, v in dic_s.items():
    # print(k, v)
    # print('dic_s:', dic_s)
    # print('dic_t:', dic_t)
    if k == '@':
        continue
    v_t = dic_t.get(k, 0)
    n_t_at = dic_t.get('@', 0)
    n_s_at = dic_s.get('@', 0)
    if v >= v_t:
        dic_s[k] = v - v_t
        dic_t[k] = 0
        if v - v_t <= n_t_at and k in target:
            dic_s[k] = 0
            dic_t['@'] = n_t_at - (v - v_t)
    else:
        dic_s[k] = 0
        dic_t[k] = v_t - v
        if v_t - v <= n_s_at and k in target:
            dic_t[k] = 0
            dic_s['@'] = n_s_at - (v_t - v)

for k, v in dic_t.items():
    # print(k, v)
    # print('dic_s:', dic_s)
    # print('dic_t:', dic_t)
    if k == '@':
        continue
    v_s = dic_s.get(k, 0)
    n_t_at = dic_t.get('@', 0)
    n_s_at = dic_s.get('@', 0)
    if v >= v_s:
        dic_t[k] = v - v_s
        dic_s[k] = 0
        # print(k, v, n_s_at, v_s)
        if v - v_s <= n_s_at and k in target:
            dic_t[k] = 0
            dic_s['@'] = n_s_at - (v - v_s)
    else:
        dic_t[k] = 0
        dic_s[k] = v_s - v
        if v_s - v <= n_t_at and k in target:
            dic_s[k] = 0
            dic_t['@'] = n_t_at - (v_s - v)

for k, v in dic_s.items():
    if k == '@':
        continue
    if v > 0:
        ans = 'No'
        break
for k, v in dic_t.items():
    if k == '@':
        continue
    if v > 0:
        ans = 'No'
        break

# print(dic_s)
# print(dic_t)

print(ans)
