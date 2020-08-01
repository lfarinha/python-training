from module.calculations import sum, substraction, division, multiplication


# import module.calculations

def runtime():
    return input('Continue? Y - N: ')


def run_script():
    number_a = int(input('Enter a number: '))
    number_b = int(input('Enter another number: '))

    operation = input('What operation do you want to do? 1-sum, 2-multiply, 3-substraction, 4-division: ')

    if operation == "1":
        print(sum(number_a, number_b))
    elif operation == "2":
        print(multiplication(number_a, number_b))
    elif operation == "3":
        print(substraction(number_a, number_b))
    elif operation == "4":
        print(division(number_a, number_b))
    elif operation == "stop":
        return "stop"
    else:
        print("Not implemented")


def run_baby_run():
    while True:
        if runtime() == 'y':
            run_script()
        else:
            break


if __name__ == '__main__':
    run_baby_run()
