from time import time
from functools import wraps
def log(filename = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            time_begin = time()
            result = func(*args, **kwargs)
            time_end = time()
            if filename == None:
                print(f"{func.__name__}: ок, затраченное время: {time_end - time_begin}")
            else:
                with open(filename, 'w') as file:
                    file.write(f"{func.__name__}: ок, затраченное время: {time_end - time_begin}")
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x/y

my_function(1, 0)