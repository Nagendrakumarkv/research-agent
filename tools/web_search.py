"""
Wikipedia search tool.

This module provides a function for retrieving a summary
from Wikipedia.
"""

from typing import Final
import wikipedia

MAX_SENTENCES: Final[int] = 5


def web_search(query: str) -> str:
    """
    Search Wikipedia and return a summary.

    Args:
        query:
            Topic to search.

    Returns:
        Summary text or an error message.
    """

    try:
        summary = wikipedia.summary(
            query,
            sentences=MAX_SENTENCES,
            auto_suggest=True
        )

        return summary

    except wikipedia.exceptions.DisambiguationError as error:
        return (
            "Multiple results found:\n"
            + ", ".join(error.options[:10])
        )

    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'."

    except Exception as error:
        return f"Search failed: {error}"