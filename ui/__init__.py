def generate_option_menu(title, *functions):
    """
    Generate basic ui for option selection and allows user to open the option page
    :param title: Title of page
    :param functions: Tuple of options that the user can select from
    :return: None
    """
    # if function is executed recursively the functions tuple contains a tuple of the functions
    # so the functions variable needs to be the tuple stored within the tuple
    if isinstance(functions[0], tuple):
        functions = functions[0]

    def invalid():
        input(f"\n{option} is not a valid input press enter to try again\n")
        generate_option_menu(title, functions)

    print(f"---{title.upper()}---")
    # print the list of valid options
    for i in range(len(functions)):
        print(f"{i+1}. {functions[i].__doc__}")
    option = input("Please select an option: ")
    # detect if the input is valid
    try:
        option = int(option)
    except ValueError:
        invalid()
        return
    if option > len(functions):
        invalid()
        return
    # execute the designated function
    print()
    functions[option-1]()


def start_main_ui():
    generate_option_menu("math maker", pure_calculator_ui, stats_calculator_ui, mechanics_calculator_ui)


def pure_calculator_ui():
    """Pure calculator"""
    print("Pure calculator")


def stats_calculator_ui():
    """Statistics calculator"""
    print("Stats calculator")


def mechanics_calculator_ui():
    """Mechanics calculator"""
    print("Mechanics calculator")

