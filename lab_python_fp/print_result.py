# Здесь должна быть реализация декоратора
def print_result(func_to_decorate):
    def decorated_func():
        result = func_to_decorate()
        print(func_to_decorate.__name__)
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

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


'''
if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
'''