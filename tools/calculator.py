"""
Calculator tool.

Safely evaluates basic mathematical expressions.
"""

from typing import Any


def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Args:
        expression:
            Mathematical expression.

    Returns:
        Result as a string.
    """

    try:
        result: Any = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception as error:
        return f"Calculation failed: {error}"