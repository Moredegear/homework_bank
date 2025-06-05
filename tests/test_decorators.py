from src.decorators import my_function
from src.decorators import example_function
from src.decorators import example_function_1
from src.decorators import my_function_1


def test_log(capsys):
    """проверяем вывод на консоль успешной операции и ошибочной"""
    my_function_1("division by zero")
    captured = capsys.readouterr()
    assert captured.out == "my_function_1 error: division by zero. Inputs: ('division by zero',), {}\n\n"
    example_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_function: ок\n\n"


def test_log2():
    """проверяем вывод в файл сообщения об ошибке"""
    my_function("error text")
    expected = open("mylog.txt", "r", encoding="utf-8").readline(90)
    assert expected == "my_function error: error text. Inputs: ('error text',), {}\n"


def test_log3():
    """проверяем вывод в файл сообщения об успехе"""
    example_function_1(1, 2)
    expected = open("mylog_1.txt", "r", encoding="utf-8").readline()
    assert expected == "example_function_1: ок\n"
