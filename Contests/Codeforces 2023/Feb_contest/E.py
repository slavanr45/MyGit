def convert(s: str) -> str:
    result, prev = '', ''
    for i in range(len(s)):
        if s[i] != prev:
            result += s[i]
            prev = s[i]
        elif s[i] == prev and result[-1] != '+':
            result += '+'
    return result


for _ in range(int(input())):
    lst = set()
    for __ in range(int(input())):
        word = input()
        if len(word) != len(set(word)):
            mix_word = convert(word)
            lst.add(mix_word)
        else:
            lst.add(word)
    print(len(lst))
