from calculator_logic import evaluate_expression


def test_addition():
    assert evaluate_expression("1+2") == "3"


def test_divide_by_zero():
    assert evaluate_expression("1/0") == "Error"


def test_invalid_expression():
    assert evaluate_expression("2+") == "Error"


def test_float_operation():
    assert evaluate_expression("3.5 * 2") == "7.0"
