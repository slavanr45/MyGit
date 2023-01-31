def find_lead(L: list) -> tuple:
    for i in range(len(L)):
        if L[i] != 0:
            result = L[i]
            L[i] = 0
            return i, result, L


for _ in range(int(input())):
    _ = input()
    lst = list(map(int, input().split()))
    while sum(lst) != 0:
        lead, val_lead, lst = find_lead(lst)
        delta = min([abs(val_lead - x) for x in lst if x != 0])
        for i in range(len(lst)):
            if abs(val_lead - lst[i]) == delta and lst[i] != 0:
                print(lead + 1, i + 1)
                lst[i] = 0
                break
    print()