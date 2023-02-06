for _ in range(int(input())):
    total, _ = map(int, input().split())
    lst = []
    for i, elem in enumerate(map(int, input().split()), 1):
        lst.append([elem, i, 0])
    # print(lst)
    lst.sort()
    # print(lst)

    prev = None
    if len(lst) > 1:
        for i in range(len(lst) - 1):
            if lst[i][0] == prev and lst[i][0] != lst[i + 1][0]:
                lst[i][0] = lst[i][0] + 1
                lst[i][2] = '+'
            elif lst[i][0] - 1 != prev:# and lst[i][0] == lst[i + 1][0]:
                lst[i][0] = lst[i][0] - 1
                if lst[i][0] < 1:
                    lst[i][0] = 1
                else:
                    lst[i][2] = '-'
            prev = lst[i][0]
        if lst[-1][0] == lst[-2][0]:
            lst[-1][0] = lst[-1][0] + 1
            lst[-1][2] = '+'
        # print(lst)
        lst.sort(key=lambda x: x[1])
        # print(lst)

        tmp = [x[0] for x in lst]
        # print(tmp)
        if max(tmp) <= total and len(tmp) == len(set(tmp)):
            result = [x[2] for x in lst]
            print(*result, sep='')
        else:
            print('x')
    else:
        if lst[0][0] == 1:
            print('0')
        elif lst[0][0]-1 <= total:
            print('-')
        else:
            print('x')
