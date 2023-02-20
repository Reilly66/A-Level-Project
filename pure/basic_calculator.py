from enum import Enum, auto


class Operations(Enum):
    POWER = auto()
    DIVISION = auto()
    MULTIPLICATION = auto()
    ADDITION = auto()
    SUBTRACTION = auto()


def basic_calculator():
    def syntax_error():
        input("Syntax error, press enter\n")
        basic_calculator()

    equation = input("Enter your equation (or 'exit' to exit):\n").replace(" ", "")
    if equation == "exit":
        return
    # convert string to a list
    equation_as_list_1 = [*equation]
    print(equation_as_list_1)
    # seperate list into individual components
    equation_as_list_2 = []
    temp = ""
    for i in range(len(equation_as_list_1)):
        if equation_as_list_1[i].isdigit() or equation_as_list_1[i] == ".":
            temp += equation_as_list_1[i]
        else:
            if temp == "":
                syntax_error()
                return
            equation_as_list_2.append(float(temp))
            equation_as_list_2.append(equation_as_list_1[i])
            temp = ""
    equation_as_list_2.append(float(temp))
    print(equation_as_list_2)

    # replace operations with enumerator
    for i in range(1, len(equation_as_list_2), 2):
        match equation_as_list_2[i]:
            case '^':
                equation_as_list_2[i] = Operations.POWER
            case '/':
                equation_as_list_2[i] = Operations.DIVISION
            case '*':
                equation_as_list_2[i] = Operations.MULTIPLICATION
            case '+':
                equation_as_list_2[i] = Operations.ADDITION
            case '-':
                equation_as_list_2[i] = Operations.SUBTRACTION
            case _:
                syntax_error()
    print(equation_as_list_2)

    answer = calculate(equation_as_list_2)


def calculate(equation):
    if len(equation) == 3:
        match equation[1]:
            case Operations.POWER:
                return equation[0]**equation[2]
            case Operations.DIVISION:
                return equation[0]/equation[2]
            case Operations.MULTIPLICATION:
                return equation[0]*equation[2]
            case Operations.ADDITION:
                return equation[0]+equation[2]
            case Operations.SUBTRACTION:
                return equation[0]-equation[2]
    else:
        pos = 0
        for i in range(len(equation)):
            if equation[i] == Operations.SUBTRACTION:
                pos = i