# -*- coding: utf-8 -*-

import datetime
from hashlib import md5


def path_to_logging(path):
    def logger(func):
        def new_func(input_file):
            start_time = datetime.datetime.now()
            res = func(input_file)
            log = '\n****************************\nФункция: ' + func.__name__ + ' стартовала: ' + str(start_time) + \
                     ' завершилась: ' + str(datetime.datetime.now()) + '\n время работы: ' + \
                     str(datetime.datetime.now() - start_time) + '\n аргументы: ' + input_file + \
                     '\nРезультат работы: \n'
            result = ''
            for start, hs in res:
                result += str(start) + ': ' + hs + '\n'
            with open(path, 'a') as file:
                file.write(log + result)
            return res
        return new_func
    return logger


@path_to_logging(input('Enter path to log file: '))
def hash_strings(file):
    start = 0
    with open(file) as f:
        list_strings = f.readlines()
    end = len(list_strings) - 1
    while start < end:
        hs = md5((list_strings[start]).encode('utf-8')).hexdigest()
        yield start, hs
        start += 1


if __name__ == '__main__':
    for start, hs in hash_strings('countries.json'):
        pass

