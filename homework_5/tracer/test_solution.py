import pytest

from solution import tracer


def make_fact():
    # собирает факториал с трассировкой для повторного использования в тестах
    @tracer
    def fact(n: int) -> int:
        if n <= 1:
            return 1
        return n * fact(n - 1)

    return fact


@pytest.mark.parametrize("n,expected,calls", [
    (0, 1, 1),
    (1, 1, 1),
    (5, 120, 5),
])
def test_fact_result_and_call_count(n, expected, calls, capsys):
    fact = make_fact()
    assert fact(n) == expected
    out = capsys.readouterr().out
    assert out.count("call fact(") == calls
    assert out.count("return fact(") == calls


def test_entry_indent_grows_with_depth(capsys):
    fact = make_fact()
    fact(3)
    lines = capsys.readouterr().out.splitlines()
    entries = [line for line in lines if "call fact(" in line]
    assert entries[0] == "call fact(3)"
    assert entries[1] == "  call fact(2)"
    assert entries[2] == "    call fact(1)"


def test_return_lines_contain_results(capsys):
    fact = make_fact()
    fact(3)
    lines = capsys.readouterr().out.splitlines()
    returns = [line for line in lines if "return fact(" in line]
    assert returns[0] == "    return fact(1) = 1"
    assert returns[1] == "  return fact(2) = 2"
    assert returns[2] == "return fact(3) = 6"


def test_depth_resets_between_calls(capsys):
    fact = make_fact()
    fact(2)
    capsys.readouterr()
    fact(2)
    lines = capsys.readouterr().out.splitlines()
    assert lines[0] == "call fact(2)"
    assert lines[-1] == "return fact(2) = 2"


def test_wraps_preserves_name():
    fact = make_fact()
    assert fact.__name__ == "fact"


def test_exception_propagates_and_resets_depth(capsys):
    @tracer
    def boom(n: int) -> int:
        if n <= 0:
            raise ValueError("bad")
        return boom(n - 1)

    with pytest.raises(ValueError):
        boom(2)
    lines = capsys.readouterr().out.splitlines()
    assert any("raise boom(0)" in line for line in lines)
    assert "raise boom(2)" in lines[-1]
    with pytest.raises(ValueError):
        boom(1)
    second = capsys.readouterr().out.splitlines()
    assert second[0] == "call boom(1)"


def test_kwargs_shown_in_call_line(capsys):
    @tracer
    def add(a: int, b: int = 0) -> int:
        return a + b

    assert add(2, b=3) == 5
    out = capsys.readouterr().out
    assert "call add(2, b=3)" in out
    assert "return add(2, b=3) = 5" in out


def test_trace_log_matches_stdout(capsys):
    fact = make_fact()
    fact(2)
    out = capsys.readouterr().out.splitlines()
    assert fact.trace_log == out
