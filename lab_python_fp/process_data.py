import json
import sys
from unique import Unique
from gen_random import gen_random
from cm_timer import cm_timer_1

path = './data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

def print_result(func_to_decorate):
    def decorated_func(arg):
        result = func_to_decorate(arg)
        print()
        if type(result) == list:
            for i in result:
                print(i)
        elif type(result) == dict:
            for i in result.keys():
                print('{} = {}'.format(i, result[i]))
        else:
            print(result)
        return result
    return decorated_func


def field(items, *args):
    assert len(args) > 0
    for i in range(len(items)):
        if len(args) == 1:
            if items[i][args[0]] != None:
                yield "{}".format(items[i][args[0]])
        else:
            flag = True
            map = dict()
            for j in range(len(args)):
                if items[i][args[j]] != None:
                    flag = False
                    map[args[j]] = items[i][args[j]]
            if not flag:
                yield map


@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, "job-name"), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: (x.startswith('программист') or x.startswith('Программист')), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return [i + ", зарплата {} руб.".format(j) for i, j in zip(arg, gen_random(len(arg), 100_000, 200_000))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))