def swap(s: str) -> int:
    h, m, s = map(int, s.split(':'))
    if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
        return h * 3600 + m * 60 + s
    raise ValueError()


for _ in range(int(input())):
    lst, flag = [], True
    for _ in range(int(input())):
        try:
            tmp_lst = tuple(map(swap, input().split('-')))
            lst.append(tmp_lst)
            start, end = tmp_lst
            assert start <= end
        except:
            flag = False

    lst = sorted(lst)
    # print(lst)
    if len(lst) > 1 and flag:
        prev_elem = lst[0]
        for cur_elem in lst[1:]:
            if prev_elem[1] >= cur_elem[0]:
                flag = False
                break
            prev_elem = cur_elem

    print('YES' if flag else 'NO')