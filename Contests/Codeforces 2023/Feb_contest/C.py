import re

for _ in range(int(input())):
    s = input()
    result = []
    while s:
        tmp = s
        if re.match('[A-Z]\d{2}[A-Z]{2}', s):
            result.append(s[:5])
            s = s[5:]
        elif re.match('[A-Z]\d{1}[A-Z]{2}', s):
            result.append(s[:4])
            s = s[4:]
        if len(s) == 0:
            print(' '.join(result))
            break
        elif tmp == s or len(s) < 4:
            print('-')
            break



