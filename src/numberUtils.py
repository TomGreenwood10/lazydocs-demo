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
