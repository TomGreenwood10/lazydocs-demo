"""Example of Google style docstrings.

Demo of doctrings.

Todo:
    - Add more functions.
    - Run formatter
"""


def multiply_positive_numbers(a: int, b: int) -> int:
    """Multiplies 2 positive numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The product of the inputs.

    Raises:
        AttributeError: If any inputs are negative.
    """
    if a < 0 or b < 0:
        raise AttributeError("Both numbers should be positive.")

    return a * b


def multiply_any_numbers(a: int, b: int) -> int:
    """Multiplies 2 numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The product of the inputs.
    """
    return a * b


def print_full_name(first_name: str, last_name: str) -> None:
    """Prints the persons full name.

    Args:
        first_name: First name.
        last_name: Lase name.

    Returns:
        The persons full name.
    """
    print(_full_name(first_name, last_name))


def _full_name(first_name: str, last_name: str) -> str:
    """Returns the persons full name.

    Args:
        first_name: First name.
        last_name: Lase name.

    Returns:
        The persons full name.
    """
    return f"{first_name} {last_name}"
