from functools import wraps


def log(filename=None):
    """декоратор проверяющий работу функции и записывающий результат в указаный файл или консоль"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__}: ок")
                    return result
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__}: ок")
                return result
            except Exception as e:
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                return e

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(error):
    raise Exception(error)


@log()
def example_function(x, y):
    return x + y


@log(filename="mylog.txt")
def example_function_1(x, y):
    return x - y
