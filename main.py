"""
CLI entry point for the Deep Research Agent.
"""

from datetime import datetime

from agent.engine import ResearchEngine
from tools.file_system import save_report


def main():

    print("=" * 70)
    print("          DEEP RESEARCH AGENT")
    print("=" * 70)

    research_goal = input(
        "\nEnter your research topic:\n\n> "
    )

    print("\n")
    print("=" * 70)
    print("Research Started...")
    print("=" * 70)

    engine = ResearchEngine()

    report = engine.run(
        research_goal
    )

    filename = (
        datetime.now().strftime(
            "research_%Y%m%d_%H%M%S"
        )
    )

    result = save_report(
        filename,
        report
    )

    print("\n")
    print("=" * 70)
    print("FINAL REPORT")
    print("=" * 70)

    print(report)

    print("\n")
    print("=" * 70)
    print(result)
    print("=" * 70)


if __name__ == "__main__":
    main()