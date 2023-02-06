for _ in range(int(input())):
    total_count = int(input())
    lst_task = map(int, input().split())
    tmp_task = [0] * total_count
    prev_task = None
    result = 'YES'

    for x in lst_task:
        if x != prev_task:
            prev_task = x
            if tmp_task[x - 1] != 0:
                result = 'NO'
                break
            else:
                tmp_task[x - 1] = 1
    print(result)