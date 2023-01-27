queries = [
    'смотреть сериалы онлайн',  # 3-1
    'новости спорта',  # 2-1
    'афиша кино',  # 2-2
    'курс доллара',  # 2-3
    'сериалы этим летом',  # 2-4
    'курс по питону',  # 3-2
    'сериалы про спорт',  # 3-3
    'засада',  # 1-1
    'Что то очень важное здесь происходит'  # 6-1

]

garbadge = {}

for query in queries:
    words = query.split()

    if len(words) in garbadge.keys():
        garbadge[len(words)] += 1
    else:
        garbadge.update({
            len(words): 1
        })

garbadge_sort = sorted(garbadge.items())

for key, value in garbadge_sort:
    percent = round((value / len(queries)) * 100, 2)
    print(f'Запрос из {key} слов: {percent}% ')