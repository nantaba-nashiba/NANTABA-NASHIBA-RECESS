from calculator import add, subtract, multiply, divide


def _parse_input(raw: str):
    """Try to convert input to int or float; otherwise return raw string to
    intentionally trigger InvalidInputError in tests.
    """
    raw = raw.strip()
    if raw == "":
        return raw
    try:
        if "." in raw:
            return float(raw)
        return int(raw)
    except ValueError:
        return raw


OPERATIONS = {
    "add": add,
    "+": add,
    "subtract": subtract,
    "-": subtract,
    "multiply": multiply,
    "*": multiply,
    "divide": divide,
    "/": divide,
}


def run_demo():
    print("Running demo test cases:\n")
    cases = [
        ("add", 1, 2),
        ("add", "one", 2),
        ("subtract", 10, 3),
        ("subtract", 5, "two"),
        ("multiply", 4, 2),
        ("multiply", "x", "y"),
        ("divide", 10, 2),
        ("divide", 5, 0),
        ("divide", "five", 0),
    ]

    for op, a, b in cases:
        fn = OPERATIONS.get(op)
        try:
            result = fn(a, b)
        except Exception as e:
            result = f"UNEXPECTED ERROR: {e}"
        print(f"{op}({a!r}, {b!r}) -> {result}")


def repl():
    print("Error-Proof Calculator CLI")
    print("Commands: add, subtract, multiply, divide, demo, exit")
    while True:
        cmd = input("op> ").strip().lower()
        if cmd in ("exit", "quit"):
            print("Goodbye")
            break
        if cmd == "demo":
            run_demo()
            continue
        if cmd not in OPERATIONS:
            print("Unknown operation. Try: add, subtract, multiply, divide, demo, exit")
            continue

        raw_a = input("a> ")
        raw_b = input("b> ")
        a = _parse_input(raw_a)
        b = _parse_input(raw_b)
        fn = OPERATIONS[cmd]
        try:
            result = fn(a, b)
        except Exception as e:
            result = f"UNEXPECTED ERROR: {e}"
        print("Result:", result)


if __name__ == "__main__":
    repl()
