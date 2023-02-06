d = {'1':4, '2':3, '3':2, '4':1}
for _ in range(int(input())):
    tmp = {}
    for x in input().split():
        tmp[x] = tmp.get(x, 0) + 1
    print('YES' if d == tmp else 'NO')

