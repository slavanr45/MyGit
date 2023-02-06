for _ in range(int(input())):  # set count
    _ = input()
    n, m = map(int, input().split())
    M = [[int(x) for x in input().split()] for _ in range(n)]
    click_count = int(input())
    lst_click = list(map(lambda x: int(x) - 1, input().split()))
    # end input data

    for click in range(click_count):  # click count
        col = lst_click[click]
        for i in range(n - 1):  # bubble sort
            for j in range(n - 1):
                if M[j][col] > M[j + 1][col]:
                    M[j], M[j + 1] = M[j + 1], M[j]
    for row in M:
        print(*row)
    print()