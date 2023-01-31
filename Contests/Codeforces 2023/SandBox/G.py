users, num_par = map(int, input().split())
d = {n: [] for n in range(1, users + 1)}
d_swap = {}

for i in range(num_par):
    a, b = map(int, input().split())
    d[a] = d.get(a) + [b]
    d[b] = d.get(b) + [a]

for key, val in d.items():
    lst = []
    for elem in val:
        lst.extend(d[elem])
    d_swap[key] = sorted(set(filter(lambda x: x != key, lst)) - set(d[key]))

for key, val in d_swap.items():
    if not val:
        print(0)
        continue
    lst = [len(set(d[elem]) & set(d[key])) for elem in val]
    max_friends = max(lst)

    for i in range(len(val)):
        if lst[i] == max_friends:
            print(val[i], end=' ')
    print()
