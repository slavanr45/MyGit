_, best_amount_ice, minutes = map(int, input().split())
lst = [[x, i] for i, x in enumerate(map(int, input().split()), 1)]
lst = sorted(lst, key = lambda x: abs(x[0]-best_amount_ice))
result_lst = []

for cur_amount, pozition in lst:
    if abs(cur_amount-best_amount_ice) <= minutes:
        minutes -= abs(cur_amount-best_amount_ice)
        result_lst.append(pozition)
    else:
        break
print(len(result_lst))
print(*result_lst)



