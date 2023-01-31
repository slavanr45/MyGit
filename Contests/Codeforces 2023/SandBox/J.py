d, cache = {}, {}  # создаем словари для данных и для кэша
raw_data = tuple(input()[::-1] for _ in range(int(input())))
for word in set(raw_data):  # сетом избавляемся от дублей в исходном словаре
    if len(word) > 3:
        d[word[:4]] = d.get(word[:4], []) + [word]
    if len(word) > 2:
        d[word[:3]] = d.get(word[:3], []) + [word]
    if len(word) > 1:
        d[word[:2]] = d.get(word[:2], []) + [word]
    d[word[0]] = d.get(word[0], []) + [word]
# print()
# print(sorted(d.items(), key=lambda x: len(x[0])))

for _ in range(int(input())):
    query = input()[::-1]  # делаем реверс введенных данных, т.к. сравнение с конца
    res = cache.get(query)  # проверяем значение в кэше
    if res:
        print(res[::-1])  # делаем обратный реверс при выводе данных на экран
    else:
        deep = min(len(query), 4)
        for val in range(deep):
            delta = deep - val
            data = d.get(query[:delta])  # делаем последовательные запросы для уменьшения выборки
            if data:  # если в словаре нет подходящих данных, расширяем запрос
                for i in range(len(query), 0, -1):
                    tmp = tuple(filter(lambda x: x[deep - 1:i] == query[deep - 1:i] and x != query, data))
                    if tmp:
                        res = tmp[0]
                        break
            if res:
                break
        else:
            res = raw_data[0]
        print(res[::-1])  # делаем обратный реверс при выводе данных на экран
        cache[query] = res  # сохраняем значение в кэш
