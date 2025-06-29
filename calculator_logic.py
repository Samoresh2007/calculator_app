def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Error"
