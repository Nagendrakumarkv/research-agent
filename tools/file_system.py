"""
File system tool.

Writes markdown reports to disk.
"""

from pathlib import Path


OUTPUT_DIRECTORY = Path("reports")


def save_report(
    filename: str,
    content: str
) -> str:
    """
    Save a markdown report.

    Args:
        filename:
            Name of the file.

        content:
            Markdown report.

    Returns:
        Success or failure message.
    """

    try:

        OUTPUT_DIRECTORY.mkdir(
            exist_ok=True
        )

        file_path = (
            OUTPUT_DIRECTORY /
            f"{filename}.md"
        )

        file_path.write_text(
            content,
            encoding="utf-8"
        )

        return f"Report saved to {file_path}"

    except Exception as error:
        return f"Failed to save report: {error}"