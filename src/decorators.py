from functools import wraps


def log(filename=None):
    """декоратор проверяющий работу функции и записывающий результат в указаный файл или консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__}: ок"
                return result
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                raise e
            finally:
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a") as file:
                        file.write(message + "\n")

        return wrapper

    return decorator
