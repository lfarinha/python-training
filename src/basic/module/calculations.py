def sum(a, b):
    print(f'Adding {a} + {b}')
    return a + b


def substraction(a, b):
    print(f'substracting {a} - {b}')
    return a - b


def multiplication(a, b):
    print(f'multiplying {a} * {b}')
    return a * b


def division(a, b):
    print(f'dividing {a} / {b}')
    if b == 0:
        return "Cannot divide by Zero"
    else:
        return a / b
