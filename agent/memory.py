"""
Memory management for the Deep Research Agent.

This module manages the short-term conversation history
using google-genai Content objects.
"""

from google.genai import types


class Memory:
    """
    Maintains conversation history for the agent.
    """

    def __init__(self) -> None:
        """
        Initialize an empty conversation history.
        """
        self._history: list[types.Content] = []

    def add_user_message(self, message: str) -> None:
        """
        Add a user message.
        """

        self._history.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=message)
                ]
            )
        )

    def add_model_message(self, message: str) -> None:
        """
        Add a model response.
        """

        self._history.append(
            types.Content(
                role="model",
                parts=[
                    types.Part.from_text(text=message)
                ]
            )
        )

    def add_tool_message(self, message: str) -> None:
        """
        Add a tool observation.

        Tool outputs are stored as user messages so the
        model can use them as new information in the next turn.
        """

        self._history.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=f"Tool Observation:\n{message}"
                    )
                ]
            )
        )

    def get_history(self) -> list[types.Content]:
        """
        Return the current conversation history.
        """

        return self._history

    def clear(self) -> None:
        """
        Remove all conversation history.
        """

        self._history.clear()