from functools import wraps


def log(filename=None):
    """декоратор проверяющий работу функции и записывающий результат в указаный файл или консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__}: ок\n"
                return result
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                return e
            finally:
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a") as file:
                        file.write(message)

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
