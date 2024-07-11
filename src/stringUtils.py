"""Utility funcitons for strings.

Part of the docstrings and lazydocs demo.

Args:
    EXAMPLE_FIRST_NAME: An example first name. Use for testing.
    EXAMPLE_LAST_NAME: An example last name. Use for testing.
"""

EXAMPLE_FIRST_NAME: str = "Mighty"
EXAMPLE_LAST_NAME: str = "Mouse"


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
