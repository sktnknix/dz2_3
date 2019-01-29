import datetime
from hashlib import md5


def path_to_logging(path):
    def logger(func):
        def new_func(*args, **kwargs):
            t = datetime.datetime.now()
            res = func(*args, **kwargs)
            result = '\n****************************\nФункция: ' + func.__name__ + ' стартовала: ' + str(t) + \
                     ' завершилась: ' + str(datetime.datetime.now()) + '\n время работы: ' + \
                     str(datetime.datetime.now() - t) + '\n аргументы: ' + str(args) + str(
                    kwargs) + '\nРезультат работы: \n' + str(res)
            with open(path, 'a') as file:
                file.write(result)
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
    file = 'countries.json'
    for start, hash in hash_strings(file):
        print(str(start) + ': ' + hash)


