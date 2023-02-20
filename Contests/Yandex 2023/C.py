import random
days = int(input())
# lst = list(map(int, input().split()))
lst = [random.randint(1, 40) for _ in range(days)]
print(lst)
result_lst = []
buy_day, sell_day = [0,0], [0,0]
prev = [lst[-1], -1]

for i in range(days-1, -1, -1):
    if lst[i] > prev[0] and sell_day[0]:
        buy_day = prev
        if buy_day[0] != sell_day[0]:
            result_lst.append([buy_day, sell_day])
        sell_day = [lst[i], i]
    if lst[i] > sell_day[0]:
        sell_day = [lst[i], i]
    prev = [lst[i], i]
    # print(f'i={i} buy_day={buy_day}, sell_day={sell_day}, prev={prev}, {result_lst}')
    # input()
if sell_day[0] and lst[0] < sell_day[0]:
    buy_day = [lst[0], 0]
    if buy_day[0] != sell_day[0]:
        result_lst.append([buy_day, sell_day])
print(f'{result_lst}')
result_lst = sorted(result_lst, key = lambda x: x[1][0] - x[0][0])#[-4:]
print(f'{result_lst}')

print(len(result_lst))
if len(result_lst):
    for x in sorted(result_lst, key = lambda x: x[0][1]):
        print(x[0][1]+1, x[1][1]+1)


