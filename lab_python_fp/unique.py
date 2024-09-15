from gen_random import gen_random


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.used_elements = set()
        self.data = list(items)
        self.index = 0
        if len(kwargs) != 0:
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                flag = True
                if type(current) == str and self.ignore_case == True:
                    for i in self.used_elements:
                        if type(i) == str and i.lower() == current.lower():
                            flag = False
                            break
                if current not in self.used_elements and flag:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


'''
data = gen_random(10, 1, 3)
for i in Unique(data, ignore_case=False):
    print(i)
'''