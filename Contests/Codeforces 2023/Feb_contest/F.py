for _ in range(int(input())):
    pages = set(range(1, int(input()) + 1))
    # print(pages)

    printed_pages = set()
    s = input()
    if (',' not in s) and ('-' not in s):
        printed_pages.add(int(s))
    elif ',' in s:
        tmp = s.split(',')
        for x in tmp:
            if (',' not in x) and ('-' not in x):
                printed_pages.add(int(x))
            else:
                start, end = map(int, x.split('-'))
                for i in range(start, end + 1):
                    printed_pages.add(int(i))
    else:
        start, end = map(int, s.split('-'))
        for i in range(start, end + 1):
            printed_pages.add(int(i))
    # print(printed_pages)

    pages.difference_update(printed_pages)
    pages = list(pages)
    # print(pages)

    if len(pages) == 1:
        print(*pages)
    else:
        start_diap = 0
        for i in range(len(pages) - 1):
            if pages[i] + 1 == pages[i + 1]:
                if start_diap == 0:
                    start_diap = pages[i]
            elif start_diap != 0:
                print(f'{start_diap}-{pages[i]}', end=',')
                start_diap = 0
            else:
                print(f'{pages[i]}', end=',')
        if start_diap != 0:
            print(f'{start_diap}-{pages[-1]}')
        else:
            print(f'{pages[-1]}')
