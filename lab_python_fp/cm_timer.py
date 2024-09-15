import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()
        return self.start

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time: {}'.format(time.time() - self.start))


@contextmanager
def cm_timer_2():
    start = time.time()
    yield start
    print('time: {}'.format(time.time() - start))


'''
with cm_timer_1():
    time.sleep(5.5)
'''