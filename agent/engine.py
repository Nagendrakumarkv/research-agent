"""
Core ReAct engine for the Deep Research Agent.
"""

from config import client, MODEL_NAME
from agent.memory import Memory

from tools.web_search import web_search
from tools.calculator import calculate


SYSTEM_PROMPT = """
You are a Deep Research Agent.

Available tools:

1. web_search
2. calculator

If a tool is required, respond EXACTLY in this format:

THOUGHT:
...

ACTION:
tool_name

INPUT:
tool_input

When enough information has been collected, respond EXACTLY like:

FINAL ANSWER:

<markdown report>

Do not invent tool results.
"""


class ResearchEngine:
    """
    Executes the ReAct loop.
    """

    def __init__(self):

        self.memory = Memory()

    def _call_model(self) -> str:
        """
        Send conversation history to Gemini.
        """

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=self.memory.get_history(),
            config={
                "system_instruction": SYSTEM_PROMPT
            }
        )

        return response.text

    def _execute_tool(
        self,
        tool_name: str,
        tool_input: str
    ) -> str:
        """
        Execute the requested tool.
        """

        if tool_name == "web_search":
            return web_search(tool_input)

        if tool_name == "calculator":
            return calculate(tool_input)

        return f"Unknown tool: {tool_name}"

    def run(
        self,
        research_goal: str
    ) -> str:
        """
        Execute the complete ReAct loop.
        """

        self.memory.clear()

        self.memory.add_user_message(research_goal)

        MAX_ITERATIONS = 10

        for _ in range(MAX_ITERATIONS):

            model_output = self._call_model()

            print("\n")
            print("=" * 60)
            print(model_output)
            print("=" * 60)

            self.memory.add_model_message(
                model_output
            )

            if model_output.startswith(
                "FINAL ANSWER:"
            ):
                return model_output.replace(
                    "FINAL ANSWER:",
                    ""
                ).strip()

            lines = model_output.splitlines()

            tool_name = ""
            tool_input = ""

            for index, line in enumerate(lines):

                if line.startswith("ACTION:"):
                    tool_name = (
                        lines[index + 1].strip()
                    )

                if line.startswith("INPUT:"):
                    tool_input = (
                        lines[index + 1].strip()
                    )

            observation = self._execute_tool(
                tool_name,
                tool_input
            )

            print("\nTOOL RESULT\n")
            print(observation)

            self.memory.add_tool_message(
                observation
            )

        return (
            "Maximum iterations reached without "
            "producing a final answer."
        )