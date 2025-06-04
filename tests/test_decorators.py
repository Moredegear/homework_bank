from src.decorators import my_function
from src.decorators import example_function
from src.decorators import example_function_1


def test_log(capsys):
    my_function("error text")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: error text. Inputs: ('error text',), {}\n"
    my_function("division by zero")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: ('division by zero',), {}\n"
    example_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_function: ок\n"
    example_function_1(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ""
