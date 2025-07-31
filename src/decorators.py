from time import time
from functools import wraps

def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                time1 = time()
                result = func(*args, **kwargs)
                time2 = time()
                name_func = func.__name__
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'Начало работы функции: {time1} \n{name_func} ок. \nРезультат: {result} \nКонец работы функции: {time2}\n\n')
                else:
                    print(f'Начало работы функции: {time1} \n{name_func} ок. \nРезультат: {result} \nКонец работы функции: {time2}\n\n')
            except TypeError:
                name_func = func.__name__
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'{name_func} error: TypeError. Inputs: {args}, {kwargs}')
                else:
                    print(f'{name_func} error: TypeError. Inputs: {args}, {kwargs}')
        return inner
    return wrapper