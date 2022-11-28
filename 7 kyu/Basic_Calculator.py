def calculate(num1, operation, num2):
    try:
        if operation == '+':
            return num1 + num2
        if operation == '-':
            return num1 - num2
        if operation == '/':
            return num1 / num2
        if operation == '*':
            return num1 * num2
    except (ZeroDivisionError, SyntaxError):
        return None
