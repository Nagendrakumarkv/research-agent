from tools.web_search import web_search
from tools.calculator import calculate
from tools.file_system import save_report


def main():

    print("=" * 60)
    print("WEB SEARCH")
    print("=" * 60)

    print(
        web_search("Artificial Intelligence")
    )

    print()

    print("=" * 60)
    print("CALCULATOR")
    print("=" * 60)

    print(
        calculate("(45 + 55) * 10")
    )

    print()

    print("=" * 60)
    print("FILE SYSTEM")
    print("=" * 60)

    print(
        save_report(
            "sample_report",
            "# Hello\n\nThis is my first report."
        )
    )


if __name__ == "__main__":
    main()