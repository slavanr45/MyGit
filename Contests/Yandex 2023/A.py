_ = input()
d = {a: b for a, b in zip(map(int, input().split()), map(int, input().split()))}
_ = input()
data_lst = map(int, input().split())

counter = 0
prev = d[next(data_lst)]
for x in data_lst:
    row = d[x]
    if row != prev:
        counter += 1
        prev = row
print(counter)

