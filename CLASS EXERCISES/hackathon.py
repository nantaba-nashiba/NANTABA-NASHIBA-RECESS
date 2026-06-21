from datetime import datetime

# 1. Custom exception
class InvalidInputError(Exception):
    """Raised when a calculator input is not a valid number."""
    pass

# 2. Simple logging setup
LOG_FILE = "log.txt"


def write_log(message):
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    with open(LOG_FILE, "a", encoding="utf-8") as handle:
        handle.write(f"{timestamp} - {message}\n")


def log_call(func):
    """Decorator that logs function calls and results."""
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            write_log(f"Called {func.__name__}(args={args}, kwargs={kwargs}) => {result}")

    return wrapper


# 3. Input validation decorator
def validate_inputs(func):
    """Decorator that validates that all positional arguments are int or float."""
    def wrapper(*args, **kwargs):
        try:
            for value in args:
                if not isinstance(value, (int, float)):
                    raise InvalidInputError(f"Invalid input: {value!r} is not a number")
            for value in kwargs.values():
                if not isinstance(value, (int, float)):
                    raise InvalidInputError(f"Invalid input: {value!r} is not a number")
            return func(*args, **kwargs)
        except InvalidInputError as exc:
            message = f"Error in {func.__name__}: {exc}"
            write_log(message)
            return message

    return wrapper


# 4. Safe divide decorator
def safe_divide(func):
    """Decorator that catches ZeroDivisionError and returns 'Infinity'."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            result = "Infinity"
            write_log(f"Division by zero in {func.__name__}(args={args}, kwargs={kwargs}) => {result}")
            return result

    return wrapper


# 5. Arithmetic functions
@log_call
@validate_inputs
def add(x, y):
    return x + y


@log_call
@validate_inputs
def subtract(x, y):
    return x - y


@log_call
@validate_inputs
def multiply(x, y):
    return x * y


@log_call
@validate_inputs
@safe_divide
def divide(x, y):
    return x / y


# 6. Testing harness
def prompt_number(prompt):
    """Read a value from the user and return a number or raw string."""
    value = input(prompt).strip()
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def main():
    print("Error-Proof Calculator API")
    print("Enter two values to test add/subtract/multiply/divide.")
    print("Type 'quit' to exit. Type 'auto' to run automated tests.")

    while True:
        first = prompt_number("First value: ")
        if isinstance(first, str) and first.lower() == "quit":
            break
        if isinstance(first, str) and first.lower() == "auto":
            test_harness()
            break
        second = prompt_number("Second value: ")
        if isinstance(second, str) and second.lower() == "quit":
            break

        print("add =>", add(first, second))
        print("subtract =>", subtract(first, second))
        print("multiply =>", multiply(first, second))
        print("divide =>", divide(first, second))
        print("---")


if __name__ == "__main__":
    main()


def test_harness():
    """Run a suite of automated tests that exercise edge cases."""
    cases = [
        (1, 2),        # normal ints
        (1, 0),        # divide by zero
        ('a', 2),      # invalid first
        (3.5, 2),      # float
        (None, 5),     # None input
        (5, 'b'),      # invalid second
        (0, 0),        # zero/zero
    ]

    print("Running automated tests:")
    for x, y in cases:
        print(f"\nInputs: {x!r}, {y!r}")
        try:
            print(" add =>", add(x, y))
        except Exception as e:
            print(" add raised:", e)
        try:
            print(" subtract =>", subtract(x, y))
        except Exception as e:
            print(" subtract raised:", e)
        try:
            print(" multiply =>", multiply(x, y))
        except Exception as e:
            print(" multiply raised:", e)
        try:
            print(" divide =>", divide(x, y))
        except Exception as e:
            print(" divide raised:", e)

    print("\nAutomated tests complete. See log.txt for recorded calls and results.")
