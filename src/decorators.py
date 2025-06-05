from functools import wraps


def log(filename=None):
    """декоратор проверяющий работу функции и записывающий результат в указаный файл или консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                d = f"{func.__name__}: ок"
                return result, d
            except Exception as e:
                d = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                return d
            finally:
                if filename is None:
                    print(d)
                else:
                    with open(filename, "w") as file:
                        file.write(d)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(error):
    raise Exception(error)


@log()
def my_function_1(error):
    raise Exception(error)


@log()
def example_function(x, y):
    return x + y


@log(filename="mylog_1.txt")
def example_function_1(x, y):
    return x - y
