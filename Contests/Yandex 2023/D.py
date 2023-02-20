count = int(input())
req_lst = tuple(zip(map(int, input().split()), map(int, input().split()), map(int, input().split()), range(1, count + 1)))
_ = input()
result_lst = []

print(req_lst)
for elem in zip(map(int, input().split()), map(int, input().split()), map(int, input().split())):
    try:
        req = next(filter(lambda x: any(((elem[2] == x[3] and x[2]), (elem[0] >= x[0] and elem[1] >= x[1]) )) ,req_lst))
    except:
        result_lst.append(0)
        continue
    result_lst.append(req[3])


print(' '.join(map(str, result_lst)))
