for _ in range(int(input())):
    __ = int(input())
    lst = map(int, input().split())
    tmp_d = []
    for i, elem in enumerate(lst):
        tmp_d.append([elem, i])
    tmp_d.sort()
    # print(tmp_d)

    result = []
    counter, add_counter = 0, 0
    prev = -2
    for x in tmp_d:
        if abs(x[0] - prev) > 1:
            counter = counter + 1 + add_counter
            add_counter = 0
        else:
            add_counter += 1
        result.append([counter, x[1]])
        prev = x[0]
    # print(result)
    for x in sorted(result, key=lambda x: x[1]):
        print(x[0], end=' ')
    print()