# -*- coding: utf-8 -*-

import datetime
import time


def path_to_logging(path):
    def logger(func):
        def new_func(*args, **kwargs):
            start_time = datetime.datetime.now()
            res = func(*args, **kwargs)
            result = '\n****************************\nФункция: ' + func.__name__ + ' стартовала: ' + str(start_time) + \
                     ' завершилась: ' + str(datetime.datetime.now()) + '\n время работы: ' + \
                     str(datetime.datetime.now() - start_time) + '\n аргументы: ' + str(args) + str(
                kwargs) + '\nРезультат работы: ' + str(res)
            with open(path, 'a') as file:
                file.write(result)
            return res
        return new_func
    return logger


@path_to_logging(input('Enter path to log file: '))
def working_func(some_string, **kwargs):
    time.sleep(1)
    kw_string = ''
    for key, value in kwargs.items():
        kw_string += ', arguments: ' + str(key) + ' ==> ' + str(value)
    return 'Entered string: ' + some_string + kw_string


some_str = input('Enter smth.: ')

working_func(some_str, kw1='kwarg1', kw2='kwarg2')
