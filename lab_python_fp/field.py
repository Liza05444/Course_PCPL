# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    for i in range(len(items)):
        if len(args) == 1:
            if items[i][args[0]] != None:
                yield "'{}'".format(items[i][args[0]])
        else:
            flag = True
            map = dict()
            for j in range(len(args)):
                if items[i][args[j]] != None:
                    flag = False
                    map[args[j]] = items[i][args[j]]
            if not flag:
                yield map


'''
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
print("Task 1: field(goods, 'title')")
test = field(goods, 'title')
print(*test, sep=', ')
print()
print("Task 2: field(goods, 'title', 'price')")
test = field(goods, 'title', 'price')
print(*test, sep=', ')
'''