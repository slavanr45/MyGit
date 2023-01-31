for _ in range(int(input())):
    num_goods = int(input())
    lst = sorted(map(int, input().split())) + [0]
    total, count = 0, 1
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            total += (count - (count // 3)) * lst[i]
            count = 1
        else:
            count += 1
    print(total)