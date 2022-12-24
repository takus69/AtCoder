S = input()
box = {}
bura = [{}]
ret = 'Yes'
for s in S:
    if s == '(':
        bura.append({})
    elif s == ')':
        for k, v in bura[-1].items():
            box[k] -= v
        del bura[-1]
    else:
        bura[-1][s] = bura[-1].get(s, 0) + 1
        box[s] = box.get(s, 0) + 1
        if box[s] > 1:
            ret = 'No'
            break
print(ret)