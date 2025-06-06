import pytest
from src.decorators import log


def func_for_test(x, y):
    """Функция для тестирования декоратора"""
    return x + y


def test_success_console(capsys):
    decorated_func = log()(func_for_test)

    result = decorated_func(1, 2)

    assert result == 3
    assert capsys.readouterr().out == "func_for_test: ок\n"


def test_error_console(capsys):
    decorated_func = log()(func_for_test)

    with pytest.raises(TypeError) as e:
        decorated_func(1, y="2")
        assert capsys.readouterr().out == f"func_for_test error: {e}. Inputs: (1,), {'y': '2'}\n"


def test_success_file(tmp_path):
    log_file = tmp_path / "test.log"
    decorated_func = log(filename=log_file)(func_for_test)

    result = decorated_func(1, 2)

    assert result == 3
    assert log_file.read_text() == "func_for_test: ок\n"


def test_error_file(tmp_path):
    log_file = tmp_path / "test.log"
    decorated_func = log(filename=log_file)(func_for_test)
    with pytest.raises(TypeError) as e:
        decorated_func(1, y="2")
        assert log_file.read_text() == f"func_for_test error: {e}. Inputs: (1,), {'y': '2'}\n"
