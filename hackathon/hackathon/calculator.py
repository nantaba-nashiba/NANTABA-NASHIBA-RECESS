import functools
import datetime
from typing import Any, Callable


class InvalidInputError(Exception):
    """Raised when an input is not an int or float."""


def _log_to_file(message: str, *, path: str = "log.txt") -> None:
    timestamp = datetime.datetime.now().isoformat()
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def log_calls(func: Callable) -> Callable:
    """Decorator that logs function calls (args, kwargs) and results to log.txt."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            # Ensure logging even if an unexpected exception occurs
            _log_to_file(f"{func.__name__} called with args={args} kwargs={kwargs} -> RAISED {exc}")
            raise
        else:
            _log_to_file(f"{func.__name__} called with args={args} kwargs={kwargs} -> {result}")
            return result

    return wrapper


def validate_inputs(func: Callable) -> Callable:
    """Decorator that validates inputs are int/float.

    If inputs are invalid it raises InvalidInputError and catches it,
    returning an error string instead of allowing the program to crash.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            for a in args:
                if not isinstance(a, (int, float)):
                    raise InvalidInputError(f"Invalid positional argument: {a}")
            for k, v in kwargs.items():
                if not isinstance(v, (int, float)):
                    raise InvalidInputError(f"Invalid keyword argument {k}={v}")
            return func(*args, **kwargs)
        except InvalidInputError as exc:
            # Catch and return a descriptive result so caller doesn't crash
            return f"InvalidInputError: {exc}"

    return wrapper


def safe_divide(func: Callable) -> Callable:
    """Decorator that catches ZeroDivisionError and returns 'Infinity'."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Infinity"

    return wrapper


# Arithmetic functions


@log_calls
@validate_inputs
def add(a: float, b: float) -> Any:
    return a + b


@log_calls
@validate_inputs
def subtract(a: float, b: float) -> Any:
    return a - b


@log_calls
@validate_inputs
def multiply(a: float, b: float) -> Any:
    return a * b


@log_calls
@validate_inputs
@safe_divide
def divide(a: float, b: float) -> Any:
    return a / b


__all__ = [
    "InvalidInputError",
    "log_calls",
    "validate_inputs",
    "safe_divide",
    "add",
    "subtract",
    "multiply",
    "divide",
]
