import number_guesser.art as art

print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation():
    should_continue = True
    print("Welcome to Calculator!")
    n1 = float(input("What's the first number?\n"))
    for sign in operations:
        print(sign)
    while should_continue:
        operator = input("Pick an operation: ")
        n2 = float(input("What's the next number?\n"))
        calc_function = operations[operator]
        answer = calc_function(n1, n2)
        print(f'{n1} {operator} {n2} = {answer}')

        more_calculation = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation. ").lower().strip()
        if more_calculation == 'y':
            n1 = answer
        else:
            should_continue = False
            calculation()


calculation()
