from tp02_1_greeting import Greeting
from tp02_2_rectangle import Rectangle
from tp02_3_equation import EquationCalculator
from tp02_4_hundreds_counter import HundredsCounter
from tp02_5_lucky_number import LuckyNumberGame

# Constants
EXIT_CHOICE = "0"
MENU_TITLE = "=========== TP02 Python OOP =========="

MENU_OPTIONS = {
    "1": "Greeting",
    "2": "Rectangle",
    "3": "Equation Calculator",
    "4": "Hundreds Counter",
    "5": "Cheater Game",
    EXIT_CHOICE: "Exit",
}

# Custom exception
class InvalidInputError(Exception):
    """Raised when user input is invalid."""

# Input helper functions
def read_number(prompt, number_type=float):
    """Read and validate a number."""
    try:
        return number_type(input(prompt))
    except ValueError:
        raise InvalidInputError("Please enter a valid number.")


def read_non_negative_number(prompt, number_type=float):
    """Read a non-negative number."""
    value = read_number(prompt, number_type)

    if value < 0:
        raise InvalidInputError("The number cannot be negative.")

    return value


# Exercise functions
def run_greeting():
    """Run the greeting exercise."""
    name = input("Enter your name: ")
    greeting = Greeting(name)
    print(greeting.get_greeting())


def run_rectangle():
    """Run the rectangle exercise."""
    width = read_non_negative_number("Enter the width: ")
    height = read_non_negative_number("Enter the height: ")

    rectangle = Rectangle(width, height)

    print(f"Perimeter: {rectangle.calculate_perimeter()}")
    print(f"Area: {rectangle.calculate_area()}")


def run_equation_calculator():
    """Run the equation calculator exercise."""
    y = read_number("Enter y: ")
    z = read_number("Enter z: ")

    if z == 0:
        raise InvalidInputError("z cannot be zero.")
    elif y == 0:
        raise InvalidInputError("y cannot be zero.")
    elif y + z == 0:
        raise InvalidInputError("y + z cannot be zero.")

    calculator = EquationCalculator(y, z)
    print(f"Calculated x: {calculator.calculate_x()}")


def run_hundreds_counter():
    """Run the hundreds counter exercise."""
    number = read_non_negative_number(
        "Enter a non-negative integer: ", int
    )

    counter = HundredsCounter(number)
    print(f"Complete hundreds: {counter.get_complete_hundreds()}")


def run_cheater_game():
    """Run the cheater game exercise."""
    number = read_number("Enter an integer: ", int)

    game = LuckyNumberGame(number)
    print(f"Result (number plus one): {game.get_next_number()}")


# Menu actions
MENU_ACTIONS = {
    "1": run_greeting,
    "2": run_rectangle,
    "3": run_equation_calculator,
    "4": run_hundreds_counter,
    "5": run_cheater_game,
}


# Menu functions
def show_menu():
    """Display the main menu."""
    print(f"\n{MENU_TITLE}")

    for choice, label in MENU_OPTIONS.items():
        print(f"{choice}. {label}")


def run_choice(choice):
    """Execute the selected menu option."""
    action = MENU_ACTIONS.get(choice)

    if action is None:
        valid_choices = ", ".join(MENU_OPTIONS)
        print(f"Invalid option! Please select: {valid_choices}")
        return

    try:
        action()
    except InvalidInputError as error:
        print(f"Invalid input! {error}")


# Main program
def main():
    """Run the TP02 Python OOP application."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == EXIT_CHOICE:
            print("Thank you for using the program. Goodbye!")
            break

        run_choice(choice)


if __name__ == "__main__":
    main()
