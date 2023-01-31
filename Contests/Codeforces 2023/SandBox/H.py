for _ in range(int(input())):
    n, m = map(int, input().split())
    M_tmp = [list(input()) for _ in range(n)]
    d = {}

    # создаем матрицу большего размера +2, для буфера на границах
    # с этим буфером проще будет проверять граничные значения при обходе
    M = [['.'] * (m + 4) for _ in range(n + 4)]
    for i in range(n):
        for j in range(m):
            if M_tmp[i][j] != '.':
                M[i + 2][j + 2] = M_tmp[i][j]
                d[M_tmp[i][j]] = 1

    # обход матрицы
    while True:
        result = 'YES'
        counter = 0
        for i in range(n):
            i = i + 2
            for j in range(m):
                j = j + 2
                if M[i][j] != '.':
                    letter = (M[i][j]).upper()
                    if d[letter] == 1 or (M[i][j]).islower():
                        d[letter] = 0
                        counter += 1
                        if M[i][j - 2].upper() == letter:
                            M[i][j - 2] = letter.lower()
                        if M[i][j + 2].upper() == letter:
                            M[i][j + 2] = letter.lower()
                        if M[i - 1][j - 1].upper() == letter:
                            M[i - 1][j - 1] = letter.lower()
                        if M[i - 1][j + 1].upper() == letter:
                            M[i - 1][j + 1] = letter.lower()
                        if M[i + 1][j + 1].upper() == letter:
                            M[i + 1][j + 1] = letter.lower()
                        if M[i + 1][j - 1].upper() == letter:
                            M[i + 1][j - 1] = letter.lower()
                        M[i][j] = '.'
                    else:
                        if counter == 0: result = 'NO'  # если нет изменений, но буквы остались
        if counter == 0: break  # выход из цикла, если в матрице нет изменений
    print(result)