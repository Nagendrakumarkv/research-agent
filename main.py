from agent.engine import ResearchEngine


def main():

    engine = ResearchEngine()

    report = engine.run(
        "Research Artificial Intelligence."
    )

    print("\n")
    print("=" * 60)
    print("FINAL REPORT")
    print("=" * 60)
    print(report)


if __name__ == "__main__":
    main()