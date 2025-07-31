from src.decorators import log


def test_log_stdout_check(capsys):
    @log()
    def add(a, b):
        return a + b

    add(2, 3)

    captured = capsys.readouterr()
    output = captured.out

    assert "add ок" in output
    assert "Результат: 5" in output
    assert "Начало работы функции:" in output
    assert "Конец работы функции" in output


def test_log_to_file(tmp_path):
    log_file = tmp_path / "text_log.txt"

    @log(str(log_file))
    def multiply(a, b):
        return a * b

    multiply(2, 7)

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "multiply ок" in content and "Результат: 14" in content and "Начало работы функции" in content


def test_log_value_error_printing(capsys):
    @log()
    def error_function():
        raise ValueError

    error_function()

    captured = capsys.readouterr()
    output = captured.out

    assert "error_function error: ValueError. Inputs: " in output


def test_log_index_error_in_file(tmp_path):
    log_file = tmp_path / "error_text.txt"

    @log(str(log_file))
    def index_error_function(ind):
        return "add"[ind]

    index_error_function(5)

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "index_error_function error: IndexError. Inputs: (5,), {}" in content
